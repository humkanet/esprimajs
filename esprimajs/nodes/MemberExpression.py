object_expressions = {
	"Identifier",
	"Literal",
	"CallExpression",
	"ThisExpression",
	"ArrayExpression",
	"ObjectExpression",
	"MemberExpression",
}

def build(node, ctx, **kwargs):
	quote_object = not (node.object.type in object_expressions)
	if quote_object: ctx.brackets(node.object, **kwargs)
	else: ctx.build(node.object, **kwargs)
	# Computed
	if node.computed:
		ctx.write("[")
		ctx.build(node.property, **kwargs)
		ctx.write("]")
	# Property
	else:
		ctx.write(".")
		ctx.build(node.property, **dict(kwargs, nomangle=True))
