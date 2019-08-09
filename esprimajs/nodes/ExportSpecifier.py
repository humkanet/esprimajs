def build(node, ctx, **kwargs):
	if node.exported.name==node.local.name: ctx.write(node.local.name)
	else:
		ctx.write(node.local.name)
		ctx.write(" as ")
		ctx.write(node.exported.name)
