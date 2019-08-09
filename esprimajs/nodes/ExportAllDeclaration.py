def build(node, ctx, **kwargs):
	ctx.write("export * from ")
	ctx.build(node.source, **kwargs)
