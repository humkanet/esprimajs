from random import choice

NUMBER_OBFUSCATORS = (
	"0o{0:o}",
	"0x{0:x}"
)


def obfuscate_number(val):
	# Value<8, cant obfuscate
	if val<8: return str(val)
	# Value<16, only ocatal obfuscator
	elif val<16: return NUMBER_OBFUSCATORS[0].format(val)
	# Else random obfuscator
	else: return choice(NUMBER_OBFUSCATORS).format(val)


def build(node, ctx, **kwargs):
	# Obfuscate string
	if isinstance(node.value, str) and ctx.config.obfuscate_strings:
		raw = ctx.obfuscate_string(node.value)
	# Bool
	elif isinstance(node.value, bool):
		raw = "!0" if node.value else "!1"
	# Number
	elif isinstance(node.value, int) and ctx.config.obfuscate_integers:
		raw = obfuscate_number(node.value)
	else: raw = node.raw
	ctx.write(raw)
