from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

setup(ext_modules=cythonize("game.pyx"), include_dirs=[numpy.get_include()])

setup(ext_modules=cythonize("pv_mcts.pyx"), include_dirs=[numpy.get_include()])

setup(name="self_play", ext_modules=[Extension("self_play", ["self_play.c"])])

# cythonize -a -i game.pyx


# cythonize -i game.pyx
# cythonize -i pv_mcts.pyx
# cythonize -i self_play.pyx
