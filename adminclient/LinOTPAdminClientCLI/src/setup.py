#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    LinOTP - the open source solution for two factor authentication
#    Copyright (C) 2010 - 2014 LSE Leading Security Experts GmbH
#
#    This file is part of LinOTP admin clients.
#
#    This program is free software: you can redistribute it and/or
#    modify it under the terms of the GNU Affero General Public
#    License, version 3, as published by the Free Software Foundation.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the
#               GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#    E-mail: linotp@lsexperts.de
#    Contact: www.linotp.org
#    Support: www.lsexperts.de
#


from distutils.core import setup
#from distutils.core import setup
#try:
#    from setuptools import setup, find_packages
#except ImportError:
#	from ez_setup import use_setuptools
#	use_setuptools()
#	from setuptools import setup, find_packages

import os
import sys

# Taken from kennethreitz/requests/setup.py
package_directory = os.path.realpath(os.path.dirname(__file__))

def get_file_contents(file_path):
    """Get the context of the file using full path name."""
    content = ""
    try:
        full_path = os.path.join(package_directory, file_path)
        content = open(full_path, 'r').read()
    except:
        print >> sys.stderr, "### could not open file %r" % file_path
    return content

setup(
    name='LinOTPAdminClientCLI',
    version='2.7.1.dev0',
    description='LinOTP command-line client',
    author='LSE Leading Security Experts GmbH',
    author_email='linotp-community@lsexperts.de',
    url='http://www.linotp.org',
    packages=['linotputils'],
    scripts=['linotpadm.py'],
     data_files=[('share/man/man1', ["linotpadm.py.1"])],
#    data_files=[('/usr/lib/python2.6/site-packages/',['linotp2-client.pth']),
#       ],
    license='AGPLv3, (C) LSE Leading Security Experts GmbH',
    long_description=get_file_contents('DESCRIPTION')
)
