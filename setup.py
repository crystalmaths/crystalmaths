"""
This is copied and adapted from https://github.com/EISy-as-Py/eisy
"""

import sys
import os
import setuptools
from setuptools import setup

# Get version and release info, which 
#is all stored in shablona/version.py

ver_file = os.path.join('crystalmaths', 'version.py')

with open(ver_file) as f:

    exec(f.read())


# Give setuptools a hint to complain if it's too old a version

# 24.2.0 added the python_requires option

# Should match pyproject.toml

# SETUP_REQUIRES = ['setuptools >= 24.2.0']
#
# # This enables setuptools to install wheel on-the-fly
#
# SETUP_REQUIRES += ['wheel'] if 'bdist_wheel' in sys.argv else []


setup(name='crystalmaths',
      description='Package for indexing the zone axis of a high res TEM image',
      description_content_type='text/markdown; \
                                charset=UTF-8; variant=GFM',
      long_description=open('README.md', 'r').read(),
      long_description_content_type='text/markdown; \
                                     charset=UTF-8; variant=GFM',
      url='https://github.com/crystalmaths/crystalmaths',
      license='MIT',
      author='Amy Stegmann, Edwin Shenjian Jiang, Elena Shoushpanova,\
              Kacper Lachowski',
      python_requires='>=3.7',
      packages=setuptools.find_packages())

classifiers = ("Programming Language :: Python :: 3",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent")
