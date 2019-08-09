def build(node, ctx, **kwargs):
	# Mangling scope
	ctx.mangler.enter()
	# For expression
	ctx.write("for(")
	if ctx.mangle_variables: ctx.mangle(node.left, "variable")
	ctx.build(node.left, **kwargs);
	ctx.write(" of ")
	ctx.build(node.right, **kwargs)
	ctx.write(")")
	ctx.build(node.body, **kwargs)
	# Mangling scope
	ctx.mangler.leave()