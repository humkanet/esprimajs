def build(node, ctx, **kwargs):
	ctx.build(node.left, **kwargs)
	ctx.write("=")
	ctx.build(node.right, **kwargs)
