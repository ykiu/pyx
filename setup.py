"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages

setup(
    name='pyx',

    # getting version info from git tags
    use_scm_version = True,
    # (the dependencies will be installed into ./.eggs/)
    setup_requires=['setuptools_scm'],

    # specifying packages to install
    packages=find_packages(),

    # dependencies
    # (the dependencies will be installed into ./.eggs/)
    install_requires=[],

    # test
    # (the dependencies will be installed into ./.eggs/)
    tests_require=[],
    test_suite='tests',

    # meta data
    author='Yusuke Kiuchi',
    description='Toy static site genetator in Python',
    long_description=open('README.rst').read(),
    url='https://github.com/ykiu/pyx/',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        "Operating System :: OS Independent",
    ],
)
