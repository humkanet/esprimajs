def build(node, ctx, **kwargs):
	# Directive
	if node.directive: ctx.write(f"\"{node.directive}\"")
	# Expression
	else: ctx.build(node.expression, **kwargs)
