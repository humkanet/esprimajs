from .mangler import Mangler
from .nodes import build_node
import io
import sys
import traceback


class EInvalidNode(Exception):
	def __init__(self, node):
		self.__node = node
	def __str__(self):
		return f"Invalid node type: {self.__node.type}"


class Context:

	NONSEMI_STATEMENTS = {
		"FunctionDeclaration",
		"SwitchStatement",
		"TryStatement",
		"ReturnStatement",
	}

	@property
	def config(self):
		return self.__config

	@property
	def idented(self):
		return self.__idented

	@property
	def minified(self):
		return not self.__idented

	@property
	def last(self):
		return self.__last

	@property
	def level(self):
		return self.__level

	@property
	def mangler(self):
		return self.__mangler

	@property
	def mangle_variables(self):
		config = self.__config.mangle_variables-1
		return config>=0 and self.mangler.level>=config

	@property
	def mangle_functions(self):
		config = self.__config.mangle_functions-1
		return config>=0 and self.mangler.level>=config



	def __init__(self, config, source=None):
		self.__config = config
		self.__writer = io.StringIO(newline="")
		self.__mangler = Mangler(prefix=config.mangle_prefix)
		self.__last = None
		self.__level = 0
		self.__source = source
		# Ident fragment, config.ident>0 = spaces, <0 = tabs
		if config.ident>0: self.__ident_fragment = " "*config.ident
		elif config.ident<0: self.__ident_fragment = "\t"
		else: self.__ident_fragment = None
		self.__idented = self.__ident_fragment is not None


	def tell(self):
		return self.__writer.tell()


	def seek(self, position):
		self.__writer.seek(position, io.SEEK_SET)


	def stream(self):
		self.__writer.seek(0, io.SEEK_SET)
		return self.__writer


	def read(self, position=0):
		self.__writer.seek(position, io.SEEK_SET)
		return self.__writer.read()


	def enter(self):
		self.__level += 1


	def leave(self):
		if self.__level>0: self.__level -= 1


	def write(self, data):
		if isinstance(data, str) and len(data)>0:
			self.__writer.write(data)
			self.__last = data[-1]


	def ident(self, data=None, prefix=None, extra=0):
		# Write prefix
		if prefix: self.write(prefix)
		# Write ident
		if self.idented:
			ident = self.__ident_fragment*(self.level+extra)
			self.write(f"\n{ident}")
		# Write data
		if data: self.write(data)


	def newline(self):
		# Ident enabled
		if self.idented: self.write("\n")


	def obfuscate_string(self, text, quotes=True):
		ob = []
		for c in text:
			code = ord(c)
			frag = f"\\x{code:02x}" if code<256 else f"\\u{code:04x}"
			ob.append(frag)
		ob = "".join(ob)
		if quotes: ob = f'"{ob}"'
		return ob


	def rearrange(self, nodes):
		# Scan variables
		enum = enumerate(nodes)
		clean = []
		for idx,node in enum:
			# Find first variable declaration
			if node.type=="VariableDeclaration":
				items = {}
				while node and node.type=="VariableDeclaration":
					# Store variable declaration
					if node.type=="VariableDeclaration":
						if node.kind not in items: items[node.kind] = node
						else:
							items[node.kind].declarations += node.declarations
							clean.append(node)
					# Next node
					idx, node = next(enum, (None, None))
		# Process groups
		if len(clean)>0:
			for node in clean: nodes.remove(node)


	def build(self, node, **kwargs):
		try:
			build_node(node, self, **kwargs)
		except Exception as e:
			start  = max(0, node.range[0]-10)
			length = min(20, node.range[1]-node.range[0])
			end    = min(node.range[0]+length, len(self.__source))
			src    = f"[line: {node.loc.start.line}, col: {node.loc.start.column}] {self.__source[start:node.range[0]]}>>>{self.__source[node.range[0]:end]}"
			print(src, file=sys.stderr)
			traceback.print_exc(limit=5)
			sys.exit(-1)


	def brackets(self, node, **kwargs):
		self.write("(")
		self.build(node, **kwargs)
		self.write(")")


	def expression(self, node, **kwargs):
		expression = {
			"Identifier",
			"Literal",
			"CallExpression",
			"ThisExpression",
			"ArrayExpression",
			"ObjectExpression",
			"MemberExpression",
		}
		quote = not (node.type in expression)
		if quote: self.write("(")
		self.build(node, **kwargs)
		if quote: self.write(")")


	def mangle(self, node, mode=None):
		# Process list
		if isinstance(node, list):
			for x in node: self.mangle(x, mode)
		#Process node with specified mode
		elif mode:
			if node.type=="Identifier":
				# Identifier already processed
				if node.name in self.mangler: return
				# Mangle identifier
				elif (
					(mode=="function" and self.mangle_functions) or
					(mode=="variable" and self.mangle_variables)
				):
					node.name = self.mangler.mangle(node.name)
					node.mangled = True
				# Save identifier
				elif node: self.mangler.append(node.name)
			elif node.type=="VariableDeclarator":
				self.mangle(node.id, mode)
				if node.init and node.init.type in {"AssignmentExpression"}: self.mangle(node.init, mode)
			elif node.type=="AssignmentExpression":
				if node.left.type in {"Identifier", "ArrayPattern"}: self.mangle(node.left, mode)
				if node.right.type=="AssignmentExpression": self.mangle(node.right, mode)
			elif node.type=="AssignmentPattern":
				self.mangle(node.left, mode)
				if node.right.type=="AssignmentExpression": self.mangle(node.right, mode)
			elif node.type=="ArrayPattern":
				self.mangle(node.elements, mode)
			elif node.type=="VariableDeclaration": self.mangle(node.declarations, "variable")
			else: raise EInvalidNode(node)
		# Process unknown mode
		else:
			if node.type=="VariableDeclaration": self.mangle(node.declarations, "variable")
			elif node.type=="FunctionDeclaration" and node.id: self.mangle(node.id, "function")
			else: raise EInvalidNode(node)



	def block(self, nodes, **kwargs):
		# Sinlgle node ?
		nodes = nodes if isinstance(nodes, list) else (nodes,)
		# First pass, collect/mangle identifiers
		for node in nodes:
			if node.type in {"VariableDeclaration", "FunctionDeclaration"}: self.mangle(node)
		# Compile block
		args = dict(kwargs, scope="block")
		for idx,node in enumerate(nodes):
			# Compile node
			self.ident()
			self.build(node, **args)
			# ReturnStatement, break block
			if node.type=="ReturnStatement": break
			# Delimiter
			if self.last!=";" and not (node.type in Context.NONSEMI_STATEMENTS):
				if self.minified: self.write(";")
				elif self.last!="}": self.write(";")


	def enum(self, nodes, delimiter=",", **kwargs):
		# Sinlgle node ?
		nodes = nodes if isinstance(nodes, list) else (nodes,)
		# Compile enum
		for idx,node in enumerate(nodes):
			# Write delimiter
			if idx>0: self.write(delimiter)
			# Compile node
			self.build(node, **kwargs)
