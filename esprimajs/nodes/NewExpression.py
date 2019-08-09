def build(node, ctx, **kwargs):
	ctx.write("new ")
	ctx.build(node.callee, **kwargs)
	# Parameters
	ctx.write("(")
	ctx.enum(node.arguments, **kwargs)
	ctx.write(")")
