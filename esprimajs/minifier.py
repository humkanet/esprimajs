# -*- coding: utf-8 -*-

from .config import Config
from .context import Context
import esprima


class Minifier:

	@property
	def config(self):
		return self.__config


	def __init__(self, **kwargs):
		self.__config = Config(**kwargs)


	def __str__(self):
		return f"{self.__class__.__name__}({self.config})"


	def minify(self, code, source="script"):
		options = dict(range=True, loc=True)
		# Parse code
		if source=="script": syntax = esprima.parseScript(code, options)
		elif source=="module": syntax = esprima.parseModule(code, options)
		elif source=="auto":
			try: syntax = esprima.parseModule(code, options)
			except:
				syntax = esprima.parseScript(code, options)
		else: raise Exception(f"Invalid source type: {source}")
		# Compile syntax
		context = Context(self.config, source=code)
		context.build(syntax)
		# Return stream
		return context.stream()
