def build(node, ctx, **kwargs):
	if node.prefix:
		ctx.write(node.operator)
		ctx.build(node.argument, **kwargs)
	else:
		ctx.build(node.argument, **kwargs)
		ctx.write(node.operator)
