#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup, Extension

if sys.argv[-1] == 'setup.py':
    print('To install, run \'python setup.py install\'')
    print()

entry_points = {
    'console_scripts': [
        'foo = hello_world.hello:foo',
        'bar = hello_world.hello:bar',
    ]
}

if __name__ == "__main__":

    setup(
        name               = 'hello-world',
        version            = '1.0',
        maintainer         = 'Himanshu Mishra',
        maintainer_email   = 'himanshumishra@iitkgp.ac.in',
        description        = 'Testing python programs',
        packages           = ['hello_world'],
        entry_points       = entry_points,
        test_suite         = 'nose.collector',
        tests_require      = ['nose>=0.10.1']
    )
