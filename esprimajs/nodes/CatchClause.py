def build(node, ctx, **kwargs):
	ctx.ident("catch(")
	ctx.build(node.param, **kwargs)
	ctx.write(")")
	ctx.build(node.body, **kwargs)
