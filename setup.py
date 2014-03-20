#!/usr/bin/env python

from setuptools import setup, Command


class Tester(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print("No tests yet")

the_scripts = []

setup (name ='pycoss',
       version = '1.0.0',
       url = 'https://github.com/kd0kfo/pycoss',
       license = 'GPL v3',
       description = 'Commonly used python code not found else where.',
       author='David Coss',
       author_email='david@davecoss.com',
       packages = ['pycoss'],
       scripts = the_scripts,
       ext_package = 'pycoss',
       cmdclass={'test': Tester})

