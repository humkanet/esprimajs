def build(node, ctx, **kwargs):
	ctx.write("continue")
	if node.label:
		ctx.write(" ")
		ctx.build(node.label, **kwargs)
