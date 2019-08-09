# -*- coding: utf-8 -*-

import io


class Writer(io.StringIO):


	@property
	def compiler(self):
		return self.__compiler

	@property
	def idented(self):
		return not self.minified

	@property
	def minified(self):
		return self.__compiler.idented<1

	@property
	def last(self):
		return self.__last


	def __init__(self, compiler):
		self.__compiler = compiler
		self.__last = None
		super().__init__(newline="")


	def write(self, data):
		super().write(data)
		self.last = data[-1]


	def ident(self, data, prefix=None, extra=0):
		# Write prefix
		if prefix: self.write(prefix)
		# Write ident
		if self.idented:
			ident = " "*(self.compiler.config.ident*(self.compiler.level+extra))
			self.write(f"\n{ident}")
		# Write data
		if data: self.write(data)


	def newline(self):
		# Ident enabled
		if self.idented: self.write("\n")
