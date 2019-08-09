def build(node, ctx, **kwargs):
	# Local = Import
	if node.imported and node.imported.name==node.local.name:
		ctx.build(node.local, **kwargs)
	# Else
	elif node.imported:
		ctx.build(node.imported, **kwargs)
		ctx.build(" as ")
		ctx.build(node.local, **kwargs)
