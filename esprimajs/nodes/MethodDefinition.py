def build(node, ctx, **kwargs):
	# Static method
	if node.static: ctx.write("static ")
	args = dict(kwargs, method=True)
	# Constructor
	if node.kind=="constructor":
		ctx.write("constructor")
		ctx.build(node.value, **args)
	# Method:
	elif node.kind=="method":
		node.value.id = node.key
		ctx.build(node.value, **args)
	# Other
	else:
		ctx.write(node.kind)
		ctx.write(" ")
		ctx.build(node.key, **kwargs)
		ctx.build(node.value, **args)
