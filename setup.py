"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='geometrio',  # Required
    version='0.0.1',  # Required
    author='Lucas Teixeira',  # Optional
    author_email='lucasteixeira.ufmg@gmail.com',  # Optional
    package_dir={'': 'geometrio'},  # Optional
    packages=find_packages(where='geometrio'),  # Required
    python_requires='>=3.5, <4',

)
