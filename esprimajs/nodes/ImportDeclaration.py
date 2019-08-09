def build(node, ctx, **kwargs):
	ctx.write("import")
	# Specifiers
	if len(node.specifiers)>0:
		bkt = False
		for n,x in enumerate(node.specifiers):
			if n>0: ctx.write(",")
			if x.type=="ImportSpecifier" and not bkt:
				ctx.write("{")
				bkt = True
			elif n==0 and x.type!="ImportSpecifier": ctx.write(" ")
			ctx.build(x, **kwargs)
		if bkt: ctx.write("}")
		ctx.write(" from")
	# Source
	ctx.write(" ")
	ctx.build(node.source, **kwargs)
