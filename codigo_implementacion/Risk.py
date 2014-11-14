#! /usr/bin/python
# -*- coding: utf-8 _*_

from readXML import *
import copy as cp

tablero = territorio()
tablero.getpais('Venezuela').tostring()
tablero.getpais(1).tostring()

print tablero.getpais('Venezuela').__class__

tableroc = cp.deepcopy(tablero)


print tablero.getvecinos('Venezuela'),'\n'

print tablero.getinfovecinos('Venezuela'),'\n'

tablero.settropasterritorio('Venezuela', 50),'\n'


