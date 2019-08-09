from esprimajs import __version__
import setuptools

with open("README.rst") as f:
	long_description = f.read()


setuptools.setup(
	name="esprimajs",
	version=__version__,
	author="kdmal",
	author_email="kdmal@yandex.ru",
	description="es6-compatible javascript minifier",
	long_description=long_description,
	long_description_content_type="text/x-rst",
	license="MIT",
	url="https://github.com/humkanet/esprimajs",
	packages=setuptools.find_packages(),
	python_requires=">=3",
	classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
	install_requires=[
		"esprima",
	]
)
