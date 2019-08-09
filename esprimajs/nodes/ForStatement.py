quote_body = {
	"EmptyStatement",
	"BlockStatement"
}


def build(node, ctx, **kwargs):
	# Mangling
	ctx.mangler.enter()
	ctx.write("for(")
	# Variable declarations
	if node.init: ctx.build(node.init, **kwargs)
	ctx.write(";")
	# Test
	if node.test: ctx.build(node.test, **kwargs)
	ctx.write(";")
	# Update
	if node.update: ctx.build(node.update, **kwargs)
	ctx.write(")")
	# Body
	ctx.build(node.body, **kwargs)
	# Mangling
	ctx.mangler.leave()
