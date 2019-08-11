def build(node, ctx, **kwargs):
	# Async function
	if node.isAsync: ctx.write("async ")
	# Name
	if node.id: ctx.build(node.id, **kwargs)
	# Mangling
	ctx.mangler.enter()
	# Parameters
	ctx.write("(")
	if ctx.mangle_variables: ctx.mangle(node.params, "variable")
	ctx.enum(node.params, **kwargs)
	ctx.write(")")
	# Arrow
	ctx.write("=>")
	# Expression/Body
	ctx.build(node.body, **kwargs)
	# Mangling scope
	ctx.mangler.leave()
