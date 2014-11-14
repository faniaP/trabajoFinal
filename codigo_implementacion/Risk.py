#! /usr/bin/python
# -*- coding: utf-8 _*_

from readXML import *
<<<<<<< HEAD
import copy as cp

tablero = territorio()
tablero.getpais('Venezuela').tostring()

tableroc = cp.deepcopy(tablero)


print tablero.getvecinos('Venezuela'),'\n'

print tablero.getinfovecinos('Venezuela'),'\n'

tablero.settropasterritorio('Venezuela', 50),'\n'

tablero.getpais('Venezuela').tostring(),'\n'

tableroc.getpais('Venezuela').tostring(),'\n'
=======
from acciones import *

territorio = territorio()
territorio.getpais('Venezuela').tostring()

#print territorio.getvecinos('Venezuela')

#print territorio.getinfovecinos('Venezuela')

territorio.settropasterritorio('Venezuela', 50)

territorio.getpais('Venezuela').tostring()

print territorio.getinfovecinos('Brasil')
>>>>>>> faniaP-master

