def build(node, ctx, **kwargs):
	ctx.write("throw ")
	ctx.build(node.argument, **kwargs)
