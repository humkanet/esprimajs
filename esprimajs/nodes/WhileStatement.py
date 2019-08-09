def build(node, ctx, **kwargs):
	ctx.write("while(")
	ctx.build(node.test, **kwargs)
	ctx.write(")")
	ctx.build(node.body, **kwargs)
