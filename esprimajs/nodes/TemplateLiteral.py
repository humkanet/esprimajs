def build(node, ctx, **kwargs):
	ctx.write("`")
	for n in range(0, len(node.quasis)):
		ctx.build(node.quasis[n], **kwargs)
		if n<len(node.expressions):
			ctx.write("${")
			ctx.build(node.expressions[n], **kwargs)
			ctx.write("}")
	ctx.write("`")