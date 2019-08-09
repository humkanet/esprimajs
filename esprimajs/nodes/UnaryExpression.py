def build(node, ctx, **kwargs):
	if node.prefix:
		ctx.write(node.operator)
		if node.operator in ["typeof", "delete", "void"]: ctx.write(" ")
		ctx.expression(node.argument, **kwargs)
