# -*- coding: utf-8 -*-

#from . import compiler
from .compiler import Compiler
import unittest


class TestExport(unittest.TestCase):
	def setUp(self):
		self.compiler = Compiler(ident=0, mangle=False)
		self.js = [
			"export{A}",
			"export{A as B}",
			"export{A,B}",
			"export{A,B as C}",
			"export let A;",
			"export let A,B;",
			"export let A,B,C=D;",
			"export default A=1;",
			"export default function(){const A=1;}",
			"export default function test(){const A=1;}",
			"export{A as default}",
			"export{A,B as default}",
			"export{B,A as default}",
			"export{A,B,C as default}",
			"export * from 'module.js';",
			"export{A} from 'module.js';",
			"export{A,B} from 'module.js';",
			"export{A as B} from 'module.js';",
			"export{A as B,C as D} from 'module.js';",
			"export{A as B,C as D,E} from 'module.js';",
			"export{X,A as B,C as D,E} from 'module.js';",
		]

	def test_case1(self):
		for js in self.js:
			out = self.compiler.module(js)
			self.assertEqual(js, out)


if __name__=="__main__":
	unittest.main()
