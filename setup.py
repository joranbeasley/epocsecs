from setuptools import setup
import os
setup(
    name='epocsecs',
    version='1.0',
    packages=['epocsecs'],
    scripts=['win/epocsec.cmd' if os.name == "nt" else 'nix/epocsec',],
    url='https://github.com/joranbeasley/epocsecs',
    license='MIT',
    author='joran',
    author_email='joranbeasley@gmail.com',
    description='a quick utility to generate epocsecs'
)
