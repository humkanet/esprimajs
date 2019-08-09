def build(node, ctx, **kwargs):
	ctx.build(node.id, **kwargs)
	if node.init:
		group = node.init.type=="SequenceExpression"
		ctx.write("=")
		if group: ctx.write("(")
		ctx.build(node.init, **kwargs)
		if group: ctx.write(")")
