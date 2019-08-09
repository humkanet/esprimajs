def build(node, ctx, **kwargs):
	raw = node.value.raw
	if ctx.config.obfuscate_strings: raw = ctx.obfuscate_string(raw, quotes=False)
	ctx.write(raw)
