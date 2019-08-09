	def compile_ExportAllDeclaration(self, node, **kwargs):
		self._write("export * from ")
		self.__compile(node.source, **kwargs)
