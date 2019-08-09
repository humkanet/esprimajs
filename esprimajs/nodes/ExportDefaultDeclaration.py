def build(node, ctx, **kwargs):
	ctx.write("export default ")
	ctx.build(node.declaration, **kwargs)
