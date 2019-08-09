def build(node, ctx, **kwargs):
	ctx.write("switch(")
	ctx.build(node.discriminant, **kwargs)
	ctx.write("){")
	ctx.enter()
	for x in node.cases:
		ctx.ident()
		ctx.build(x, **kwargs)
	ctx.leave()
	ctx.ident("}")
