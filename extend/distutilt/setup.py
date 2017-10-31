
from distutils.core import setup, Extension

setup(name='helloPackage', version='1.0', ext_modules=[Extension('_hello', ['hello.c'])])

