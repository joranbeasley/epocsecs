from setuptools import setup
import os
setup(
    name='epocsecs',
    version='1.0',
    py_modules=['epocsecs'],
    # scripts=['scripts/win/epocsec.cmd' if os.name == "nt" else 'scripts/nix/epocsec',],
    entry_points="""
        [console_scripts]
        decasec=epocsecs:parse_args
        epocsec=epocsecs:parse_args        
    """,
    url='https://github.com/joranbeasley/epocsecs',
    license='MIT',
    author='joran',
    author_email='joranbeasley@gmail.com',
    install_requires=['python-dateutil'],
    description='a quick utility to generate epocsecs'
)
