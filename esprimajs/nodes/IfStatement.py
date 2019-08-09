statements = {
	"BlockStatement",
	"TryStatement",
	"IfStatement",
}


def build(node, ctx,**kwargs):
	ctx.write("if(")
	ctx.build(node.test, **kwargs)
	ctx.write(")")
	ctx.build(node.consequent, **kwargs)
	if node.alternate:
		if not (node.consequent.type in statements) and ctx.last!=";": ctx.write(";")
		ctx.ident("else")
		if node.alternate.type!="BlockStatement": ctx.write(" ")
		ctx.build(node.alternate, **kwargs)
