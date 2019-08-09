def build(node, ctx, **kwargs):
	# Test fragment
	if node.test:
		ctx.write(f"case ")
		ctx.build(node.test, **kwargs)
	else: ctx.write("default")
	ctx.write(":")
	# Body
	ctx.enter()
	ctx.block(node.consequent, **kwargs)
	ctx.leave()

