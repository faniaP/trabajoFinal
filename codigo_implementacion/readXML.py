#! /usr/bin/python
# -*- coding: utf-8 _*_

import xml.etree.ElementTree as ET
from Node import *

class territorio:
    
    ###########################################
    # Por medio de este modulo es que podemos #
    # generar un parser para un archivo xml   #
    # y cargar la grafica de nuestro          #
    # territorio de juego.                    #
    # Fernando Abigail Galicia Mendoza        #
    # Estefania Prieto Larios                 #
    # Antonio Galvan                          #
    ###########################################
    
    def __init__(self):
        '''
        Metodo encargado de generar el arbol que 
        se encuentra definido en el archivo .xml
        '''
        self.listOfNodes = []
        territorio = ET.parse('Territorio.xml')
        arbol = territorio.getroot()
        
        for node in arbol:
            vecinos = [x.text for x in node.findall('vecino')]
            nodo = Node(node.attrib['nombre'], node.find('id').text, 
                        node.find('continente').text,
                        node.find('tropas').text,
                        node.find('jugador').text,vecinos)
            
            self.listOfNodes.append(nodo)
            
    def getpais(self, nombre):
        for pais in self.listOfNodes:
            if pais.getnombre() == nombre:
                return pais
            else:
                continue
        print 'Pais no valido dentro del territorio de juego'
        return None
    
        
    def getInformacionVecinos(self, pais):
        '''Devuelve la información de los vecinos del pais dado'''
        espia = [vecinos for vecinos in ]
        print espia
        
