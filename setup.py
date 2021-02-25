from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

setup(ext_modules=cythonize("game.pyx"), include_dirs=[numpy.get_include()])

setup(ext_modules=cythonize("pv_mcts.pyx"), include_dirs=[numpy.get_include()])

setup(ext_modules=cythonize("self_play.pyx"), include_dirs=[numpy.get_include()])


# extensions = [
#     Extension(
#         "self_play",
#         ["self_play.pyx"],
#         extra_compile_args=["-fopenmp"],
#         extra_link_args=["-fopenmp"],
#     )
# ]
# setup(ext_modules=cythonize(extensions))


# cythonize -a -i game.pyx


# cythonize -i game.pyx
# cythonize -i pv_mcts.pyx
# cythonize -i self_play.pyx
