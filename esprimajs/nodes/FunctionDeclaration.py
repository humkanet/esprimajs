def build(node, ctx, **kwargs):
	# Async function
	if node.isAsync: ctx.write("async ")
	# Function
	ctx.write("function")
	# Function name
	if node.id:
		ctx.write(" ")
		ctx.build(node.id, **kwargs)
	# Mangling
	ctx.mangler.enter()
	# Function parameters
	ctx.write("(")
	ctx.mangle(node.params, "variable")
	ctx.enum(node.params, **kwargs)
	ctx.write(")")
	# Function body
	if node.body:
		ctx.build(node.body, **kwargs)
	else: ctx.write(";")
	# Mangling
	ctx.mangler.leave()
