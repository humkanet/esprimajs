def build(node, ctx, **kwargs):
	ctx.expression(node.callee)
	ctx.write("(")
	ctx.enum(node.arguments, **kwargs)
	ctx.write(")")
