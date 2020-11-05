import os
from setuptools import setup, find_packages

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
VERSION_FILE = os.path.join(BASE_DIR, 'uw_saml2', 'VERSION')
with open(VERSION_FILE) as f:
    VERSION = f.readlines()[-1].strip()

with open(os.path.join(BASE_DIR, 'README.md')) as f:
    LONG_DESCRIPTION = f.read()

saml_requires = ['python3-saml']
tests_require = saml_requires + ['pytest', 'pytest-cov', 'mock', 'pycodestyle']

setup(name='uw-saml',
      version=VERSION,
      url='https://github.com/UWIT-IAM/uw-saml-python',
      author='UW-IT Identity and Access Management',
      author_email='help@uw.edu',
      description='A UW-specific adapter to the python3-saml package.',
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/markdown',
      license='Apache License, Version 2.0',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['Werkzeug', 'cachelib'],
      extras_require={'python3-saml': saml_requires, 'test': tests_require}
      )
