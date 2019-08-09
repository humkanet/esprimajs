def build(node, ctx, **kwargs):
	ctx.write("[")
	ctx.enum(node.elements)
	ctx.write("]")
