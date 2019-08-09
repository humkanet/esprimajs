def build(node, ctx, **kwargs):
	ctx.write("...")
	ctx.build(node.argument, **kwargs)
