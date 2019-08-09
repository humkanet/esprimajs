def build(node, ctx, **kwargs):
	# Write head
	ctx.write("export")
	# Specifiers
	if isinstance(node.specifiers, list) and len(node.specifiers)>0:
		ctx.write("{")
		ctx.enum(node.specifiers, **kwargs)
		ctx.write("}")
	# Declaration
	if node.declaration:
		ctx.write(" ")
		ctx.build(node.declaration, **kwargs)
	# Source
	if node.source:
		ctx.write(" from ")
		ctx.build(node.source, **kwargs)
