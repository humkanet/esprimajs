def build(node, ctx, **kwargs):
	ctx.build(node.left, **kwargs)
	ctx.write(node.operator)
	ctx.build(node.right, **kwargs)
