def build(node, ctx, **kwargs):
	ctx.write("break")
	if node.label:
		ctx.write(" ")
		ctx.build(node.label, **kwargs)
