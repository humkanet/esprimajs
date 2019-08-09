quote_expressions = {
	"AssignmentExpression",
	"SequenceExpression"
}

operators = {
	"||", "&&"
}


def build(node, ctx, **kwargs):
	args = dict(kwargs, operator=node.operator)
	def quoted(x):
		q = x.type in quote_expressions
		if q: ctx.write("(")
		ctx.build(x, **args)
		if q: ctx.write(")")
	prev = kwargs.get("operator")
	group = (prev in operators) and (prev!=node.operator)
	if group: ctx.write("(")
	quoted(node.left)
	ctx.write(node.operator)
	quoted(node.right)
	if group: ctx.write(")")
