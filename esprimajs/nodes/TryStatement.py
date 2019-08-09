def build(node, ctx, **kwargs):
	ctx.write("try")
	ctx.build(node.block, **kwargs)
	if node.handler: ctx.build(node.handler, **kwargs)
	if node.finalizer:
		ctx.ident("finally{")
		ctx.enter()
		ctx.build(node.finalizer, **kwargs)
		ctx.leave()
		ctx.write("}")
