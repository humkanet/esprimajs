quote_expressions = {
	"SequenceExpression",
}


def build(node, ctx, **kwargs):
	def quoted(x):
		q = x.type in quote_expressions
		if q: ctx.write("(")
		ctx.build(x, **kwargs)
		if q: ctx.write(")")
	quoted(node.test)
	ctx.write("?")
	quoted(node.consequent)
	ctx.write(":")
	quoted(node.alternate)
