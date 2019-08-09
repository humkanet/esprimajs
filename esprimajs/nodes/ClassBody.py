def build(node, ctx, **kwargs):
	ctx.enter()
	ctx.block(node.body, **kwargs)
	ctx.leave()
