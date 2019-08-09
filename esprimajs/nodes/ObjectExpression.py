def build(node, ctx, **kwargs):
	# Open bracket
	ctx.write("{")
	# Compile nodes
	if isinstance(node.properties, list):
		ctx.enter()
		for idx,x in enumerate(node.properties):
			if idx>0: ctx.write(",")
			ctx.ident()
			ctx.build(x, **kwargs)
		ctx.leave()
	# Close bracket
	ctx.write("}")
