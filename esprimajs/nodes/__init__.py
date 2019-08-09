# -*- coding: utf-8 -*-

NODES = [
	# Other
	"ArrayPattern",
	"AssignmentPattern",
	"CatchClause",
	"ClassBody",
	"ClassDeclaration",
	"ExportNamedDeclaration",
	"ExportSpecifier",
	"FunctionDeclaration",
	"Identifier",
	"ImportDeclaration",
	"ImportDefaultSpecifier",
	"ImportNamespaceSpecifier",
	"ImportSpecifier",
	"Literal",
	"MethodDefinition",
#	"ObjectPattern",
	"Program",
	"Property",
	"RestElement",
	"Super",
	"SwitchCase",
	"TemplateElement",
	"TemplateLiteral",
	"VariableDeclaration",
	"VariableDeclarator",
	# Expressions
	"ArrayExpression",
	"ArrowFunctionExpression",
	"AssignmentExpression",
	"BinaryExpression",
	"CallExpression",
	"ClassExpression",
	"ConditionalExpression",
	"ExportDefaultDeclaration",
	"FunctionExpression",
	"LogicalExpression",
	"MemberExpression",
	"NewExpression",
	"ObjectExpression",
	"SequenceExpression",
	"ThisExpression",
	"UnaryExpression",
	"UpdateExpression",
	# Statements
	"BlockStatement",
	"BreakStatement",
	"ContinueStatement",
	"EmptyStatement",
	"ExpressionStatement",
	"ForInStatement",
	"ForOfStatement",
	"ForStatement",
	"IfStatement",
	"ReturnStatement",
	"SwitchStatement",
	"ThrowStatement",
	"TryStatement",
	"WhileStatement"
]

BINDING = {}

import importlib
for name in NODES:
	module = importlib.import_module(f".{name}", __package__)
	if hasattr(module, "build"):
		BINDING[name] = getattr(module, "build")


def build_node(node, context=None, **kwargs):
	f = BINDING.get(node.type)
	if not callable(f):
		raise Exception(f"Node not supported: {node.type}")
	f(node, context, **kwargs)
