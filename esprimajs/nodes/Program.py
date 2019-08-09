def build(node, ctx, **kwargs):
	if ctx.config.rearrange: ctx.rearrange(node.body)
	ctx.block(node.body, **kwargs)
