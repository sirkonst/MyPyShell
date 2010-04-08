#!/usr/bin/env python

from distutils.core import setup

setup(name='Shell',
      version='0.0.1',
      description='Shell execute',
      long_description = "My shell execute",
      author="Konstantin vz'One Enchant",
      author_email='sirkonst@gmail.com',
      url='http://wiki.enchtex.info',
      packages = ['shell'],
      package_dir = {'shell': 'src/shell'},
     )