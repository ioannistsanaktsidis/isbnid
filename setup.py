#!/usr/bin/env python

from setuptools import setup


extras_require = {
    'tests': [
        'pytest-pep8>=1.0.6',
        'pytest>=3.0.4'
    ],
}


extras_require['all'] = []
for _name, reqs in extras_require.items():
    extras_require['all'].extend(reqs)

setup(
    name='isbnid_fork',
    author='ISBNid GitHub',
    author_email='admin@inspirehep.net',
    description="Python ISBN ids",
    license="GPL",
    version="0.5.2",
    url='https://github.com/inspirehep/isbnid',
    keywords='ISBN',
    extras_require=extras_require,
    packages=['isbn'],
    package_dir={
        'isbn': 'isbn'},
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Indexing",
    ],
)
