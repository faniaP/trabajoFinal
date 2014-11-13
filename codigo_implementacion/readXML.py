#! /usr/bin/python
# -*- coding: utf-8 _*_

import xml.etree.ElementTree as ET
from Node import *

###########################################
# Por medio de este modulo es que podemos #
# generar un parser para un archivo xml   #
# y cargar la grafica de nuestro          #
# territorio de juego.                    #
# Fernando Abigail Galicia Mendoza        #
# Estefania Prieto Larios                 #
# Antonio Galvan                          #
###########################################

def loadXML():
    '''
    Metodo encargado de generar el arbol que 
    se encuentra definido en el archivo .xml
    '''
    territorio = ET.parse('Territorio.xml')
    arbol = territorio.getroot()

    listOfNodes = []

    for node in arbol:
        vecinos = [x.text for x in node.findall('vecino')]
        nodo = Node(node.attrib['nombre'], node.find('id').text, 
                    node.find('continente').text,node.find('tropas').text,
                    node.find('jugador').text,vecinos)

        listOfNodes.append(nodo)

    for elem in listOfNodes:
        elem.tostring()

loadXML()
