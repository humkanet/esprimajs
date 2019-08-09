def build(node, ctx, **kwargs):
	# Async function
	if node.isAsync: ctx.write("async ")
	# Name
	if node.id: ctx.build(node.id, **kwargs)
	# Mangling
	ctx.mangler.enter()
	# Parameters
	ctx.write("(")
	ctx.enum(node.params, **kwargs)
	ctx.write(")")
	# Arrow
	ctx.write("=>")
	# Expression/Body
	ctx.build(node.body, **kwargs)
	# Mangling scope
	ctx.mangler.leave()
