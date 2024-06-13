from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from importlib.machinery import SourceFileLoader
from pathlib import Path
import os

project_root = Path(__file__).parent
pygments_shader_root = project_root / "pygments_shader"

version = SourceFileLoader("pygments_shader.version", str(pygments_shader_root / "version.py")).load_module()

setup(
    name='pygments-shader',
    version=version.__version__,
    description='Pygments lexer for Unity shader',
    long_description=open('README.rst').read(),
    url='https://github.com/midnightSuyama/pygments-shader',
    author='midnightSuyama',
    author_email='midnightSuyama@gmail.com',
    license='MIT',
    classifiers=[
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License'
    ],
    keywords='pygments shader unity',
    packages=find_packages(exclude=['tests*']),
    install_requires=['Pygments'],
    entry_points={'pygments.lexers': 'shader=pygments_shader:ShaderLexer'},
    tests_require=['pytest']
)
