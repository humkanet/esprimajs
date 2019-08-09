def build(node, ctx, **kwargs):
	ctx.write("return")
	if node.argument:
		ctx.write(" ")
		ctx.build(node.argument, **kwargs)
