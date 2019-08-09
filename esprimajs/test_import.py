# -*- coding: utf-8 -*-

#from . import compiler
from .compiler import Compiler
import unittest


class TestImport(unittest.TestCase):
	def setUp(self):
		self.compiler = Compiler(ident=0, mangle=False)
		self.js = [
			"import 'module.js';",
			"import A from 'module.js';",
			"import{A as B} from 'module.js';",
			"import{A,B} from 'module.js';",
			"import{A,B as C} from 'module.js';",
			"import * as A from 'module.js';",
			"import A,{B,C} from 'module.js';"
			"import A,{B,C as D} from 'module.js';"
			"import A,* as B from 'module.js';"
		]

	def test_case1(self):
		for js in self.js:
			out = self.compiler.module(js)
			self.assertEqual(js, out)


if __name__=="__main__":
	unittest.main()
