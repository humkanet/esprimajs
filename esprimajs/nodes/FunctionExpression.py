def build(node, ctx, **kwargs):
	# Mangling
	ctx.mangler.enter()
	# Async
	if node.isAsync: ctx.write("async ")
	# Method
	if not kwargs.get("method"):
		ctx.write("function")
		if node.id: ctx.write(" ")
	# Skip function name
	if node.id: ctx.build(node.id, **kwargs)
	# Parameters
	ctx.write("(")
	ctx.mangle(node.params, "variable")
	ctx.enum(node.params, **kwargs)
	ctx.write(")")
	# Body
	ctx.build(node.body, **kwargs)
	# Mangling
	ctx.mangler.leave()
