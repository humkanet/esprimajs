def build(node, ctx, **kwargs):
	ctx.write("* as ")
	ctx.build(node.local, **kwargs)
