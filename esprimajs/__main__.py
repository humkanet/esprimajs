# -*- coding: utf-8 -*-

import sys
import argparse
from . import minify


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("src", type=argparse.FileType("r"), default="-", help="Source, default '%(default)s'", nargs="?")
	parser.add_argument("-d", dest="dst",  metavar="path", type=argparse.FileType("w"), default="-", help="Destination, default '%(default)s'", nargs="?")
	parser.add_argument("-s", type=str, dest="source", default="auto", choices=["script", "module", "auto"], help="Source type, default '%(default)s'")
	parser.add_argument("-r", action="store_true", dest="rearrange", default=False, help="Rearrange variables")
	parser.add_argument("-i", dest="ident", metavar="ident", type=int, default=2, help="Ident output (default %(default)d, use 0 for disable identing)")
	parser.add_argument("-mp", "--mangle-prefix", metavar="prefix", type=str, default="$", help="Mangle prefix (default: %(default)s)")
	parser.add_argument("-mv", "--mangle-variables", type=int, metavar="n", default=False, help="Start mangling variables from level '%(metavar)s' (default: %(default)d, 0 - disable)")
	parser.add_argument("-mf", "--mangle-functions",  type=int, metavar="n", default=False, help="Start mangling functions from level '%(metavar)s' (default: %(default)d, 0 - disable)")
	parser.add_argument("-os", "--obfuscate-strings", action="store_true", default=False, help="Obfuscate strings")
	parser.add_argument("-oi", "--obfuscate-integers", action="store_true", default=False, help="Obfuscate integers")
	args = parser.parse_args()

	# Read source
	code = args.src.read()

	# Compile
	buf = minify(code, **vars(args))

	# Display buffer
	args.dst.write(buf.read())
	buf.close()


if __name__=="__main__":
	retval = main()
	sys.exit(retval)
