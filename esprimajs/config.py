# -*- coding: utf-8 -*-

PARAMETERS = dict(
	ident=0,
	rearrange=False,
	mangle_prefix="$",
	mangle_variables=0,
	mangle_functions=0,
	obfuscate_strings=False,
	obfuscate_integers=False
)


class Config:

	def __init__(self, **kwargs):
		# Get parameters
		args = { x: kwargs[x] if x in kwargs else PARAMETERS[x] for x in PARAMETERS }
		# Force defaults
		if not "ident" in args: args[ident] = 0
		# Store parameters
		self.__args = args


	def __getattr__(self, name):
		return self.__args.get(name)


	def __str__(self):
		args = { k:v for k,v in self.__args.items() if self.__args[k]!=PARAMETERS[k] }
		return ", ".join([ f"{k}={v}" for k,v in args.items() ])
