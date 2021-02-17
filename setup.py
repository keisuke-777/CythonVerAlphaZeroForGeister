from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

setup(ext_modules=cythonize("game.pyx"), include_dirs=[numpy.get_include()])


# cythonize -a -i game.pyx


# cythonize -i game.pyx
# cythonize -i pv_mcts.pyx
# cythonize -i self_play.pyx
