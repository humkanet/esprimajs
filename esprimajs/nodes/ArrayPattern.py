def build(node, ctx, **kwargs):
	ctx.write("[")
	ctx.enum(node.elements, **kwargs)
	ctx.write("]")
