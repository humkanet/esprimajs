def build(node, ctx, **kwargs):
	ctx.enum(node.expressions, **kwargs)
