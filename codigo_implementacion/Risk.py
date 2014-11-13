#! /usr/bin/python
# -*- coding: utf-8 _*_

from readXML import *

territorio = territorio()
territorio.getpais('Venezuela').tostring()

#print territorio.getvecinos('Venezuela')

#print territorio.getinfovecinos('Venezuela')

territorio.settropasterritorio('Venezuela', 50)

territorio.getpais('Venezuela').tostring()

print territorio.getinfovecinos('Brasil')
