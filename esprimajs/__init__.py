__version__ = "0.1.0"

from .minifier import Minifier


def minify(code, source="auto", **kwargs):
	c = Minifier(**kwargs)
	return c.minify(code, source=source)
