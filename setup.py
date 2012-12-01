#!/usr/bin/env python
# - title        : Setup for Uploader using CloudFiles
# - description  : Want to upload a bunch files to cloudfiles? This will do it.
# - License      : GPLv3+
# - author       : Kevin Carter
# - date         : 2011-11-09
# - usage        : python setup.py install
# - notes        : This is a CloudFiles Upload Script
# - Python       : >= 2.6

"""
License Inforamtion
    
This software has no warranty, it is provided 'as is'. It is your responsibility
to validate the behavior of the routines and its accuracy using the code provided.
Consult the GNU General Public license for further details (see GNU General Public License).
    
http://www.gnu.org/licenses/gpl.html
"""

import os
import setuptools
import sys
import turbolift


if sys.version_info < (2, 6, 0):
    sys.stderr.write("Turbolift Presently requires Python 2.6.0 or greater \n")
    sys.exit('\nYou should upgrade because you version of python is VERY deprecated\n')


turbolift_modules = ['argparse', 'datetime']


def read_file(file_name):
    return open(os.path.join(os.path.dirname(__file__),
                file_name)).read()


setuptools.setup(
    name='turbolift',
    version='0.9',
    author='Kevin Carter',
    author_email='kevin@bkintegration.com',
    description='OpenStack Swift -Cloud Files- Uploader'
        ,
    long_description=read_file('README.rst'),
    license='GPLv3',
    packages=['turbolift'],
    url='https://github.com/cloudnull/turbolift.git',
    install_requires=turbolift_modules,
    classifiers=[
              "Development Status :: RC6a",
              "Intended Audience :: Devlopers and Users",
              "Intended Audience :: Information Technology",
              "License :: GPLv3",
              "Operating System :: OS Independent",
              "Programming Language :: Python",
              ],
    entry_points={
    "console_scripts": ["turbolift = turbolift.executable:run_turbolift"]
    }
)
