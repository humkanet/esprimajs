def build(node, ctx, **kwargs):
	ctx.write("class")
	# Class name
	if node.id:
		ctx.write(" ")
		ctx.build(node.id, **kwargs)
	# Super class
	if node.superClass:
		ctx.write(" extends ")
		ctx.build(node.superClass)
	# Class body
	ctx.write("{")
	ctx.build(node.body)
	ctx.ident("}")
