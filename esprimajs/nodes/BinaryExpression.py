quote_expressions = {
	"AssignmentExpression",
	"SequenceExpression",
	"ConditionalExpression"
}

operators = {
	"instanceof", "in",
	"+", "-", "*", "/", "%", "**" ,
	"|", "^", "&", "==",
	"!=", "===", "!==" ,
	"<", ">", "<=", "<<", ">>", ">>>"
}


def build(node, ctx, **kwargs):
	args = dict(kwargs, operator=node.operator)
	def quoted(x, operator=None):
		q = x.type in quote_expressions
		if q: ctx.write("(")
		ctx.build(x, **args)
		if q: ctx.write(")")
	# Operator for "instanceof", "in"
	if node.operator in ["instanceof", "in"]: op = f" {node.operator} "
	else: op = node.operator
	# Group operands
	prev = kwargs.get("operator")
	group = (prev in operators) and (prev!="+")
	if group: ctx.write("(")
	quoted(node.left)
	ctx.write(op)
	quoted(node.right)
	if group: ctx.write(")")
