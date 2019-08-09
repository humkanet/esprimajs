def build(node, ctx, **kwargs):
	ctx.write(f"{node.kind} ")
	scope = kwargs.get("scope")
	for idx,x in enumerate(node.declarations):
		if idx>0:
			ctx.write(",")
			if scope=="block": ctx.ident(extra=1)
		ctx.build(x, **kwargs)
