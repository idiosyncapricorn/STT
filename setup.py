from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("speech_recognition_cython.pyx"),
)