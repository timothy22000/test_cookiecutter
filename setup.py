#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Timothy Sum",
    author_email='timothy22000@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="testing out cookiecutter",
    entry_points={
        'console_scripts': [
            'src=src.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='test-cookiecutter100',
    name='test-cookiecutter100',
    packages=find_packages(include=['*', 'src.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/timothy22000/test_cookiecutter',
    version='0.1.1',
    zip_safe=False,
)
