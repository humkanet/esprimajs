def build(node, ctx, **kwargs):
	# Rearrange variables
	if ctx.config.rearrange: ctx.rearrange(node.body)
	# Open bracket
	ctx.write("{")
	ctx.enter()
	# Compile nodes
	ctx.block(node.body, **kwargs)
	# Close bracket
	ctx.leave()
	ctx.ident("}")
