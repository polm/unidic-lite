import setuptools
from distutils.core import setup
from io import open

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    README = f.read()

setup(name='unidic-lite', 
      version='1.0.7a1',
      author="Paul O'Leary McCann",
      author_email="polm@dampfkraft.com",
      description="A small version of UniDic packaged for Python",
      long_description=README,
      long_description_content_type="text/markdown",
      url="https://github.com/polm/unidic-lite",
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: Japanese",
      ],
      package_data={'unidic_lite': ['dicdir/*']}
      )
