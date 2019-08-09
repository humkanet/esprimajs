def build(node, ctx, **kwargs):
	# Get identifier
	declare = kwargs.get("declare")
	# No mangling
	if "nomangle" in kwargs: name = node.name
	# Mangled identifier
	elif node.mangled: name = node.name
	# Demangle
	else: name = ctx.mangler.demangle(node.name)
	# Write wariable name
	ctx.write(name)
#	if name!=node.name: ctx.write(f"/* mangle: {name} => {node.name} */")
