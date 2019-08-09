def build(node, ctx, **kwargs):
	# Computed
	if node.computed: ctx.write("[")
	# Key
	ctx.build(node.key, **dict(kwargs, nomangle=True))
	# Computed
	if node.computed: ctx.write("]")
	# Value
	if node.value:
		if not node.method:
			ctx.write(":")
			ctx.build(node.value, **kwargs)
		else: ctx.build(node.value, **dict(kwargs, method=True))
