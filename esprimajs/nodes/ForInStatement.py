def build(node, ctx, **kwargs):
	# Mangling
	ctx.mangler.enter()
	# For statement
	ctx.write("for(")
	ctx.build(node.left, **kwargs)
	ctx.write(" in ")
	ctx.build(node.right, **kwargs)
	ctx.write(")")
	ctx.build(node.body, **kwargs)
	# Mangling
	ctx.mangler.leave()
