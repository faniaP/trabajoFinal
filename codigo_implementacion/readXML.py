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
            nodo = Node(node.attrib['nombre'], int(node.find('id').text), 
                        node.find('continente').text,
                        int(node.find('tropas').text),
                        node.find('jugador').text,vecinos)
            
            self.listOfNodes.append(nodo)
            
    def getpais(self, llave):
        '''Regresa el pais con la llave deseada, en caso de no existir, nulo'''
        if type(llave) == str:
            for pais in self.listOfNodes:
                if pais.getnombre() == llave:
                    return pais
                else:
                    continue
        else: 
            if type(llave) == int:
                for pais in self.listOfNodes:
                    if pais.getid() == llave:
                        return pais
                    else:
                        continue
                
        print 'Pais no valido dentro del territorio de juego'
        return None
    

    def getvecinos(self, nombre):
        '''Regresa la lista de vecinos de un pais'''
        return self.getpais(nombre).getvecinos()
        
    def getinfovecinos(self, pais):
        '''Devuelve la información de los vecinos del pais dado'''
        espiados = self.getvecinos(pais)
        informacion = []
        for espiado in espiados:
            tmp = self.getpais(espiado)
            informacion.append({'nombre' : tmp.getnombre(), 
                                'id' : tmp.getid(), 'jugador' : tmp.getjugador(),
                                'tropas' : tmp.gettropas()})
        
        return informacion

    def settropasterritorio(self, pais, num_tropas):
        '''Actualiza la cantidad de tropas en el pais deseado'''
        self.getpais(pais).settropas(num_tropas)

    def todosnovisitados():
        '''Marca todos los nodos como no visitados'''
        for node in self.listOfNodes:
            node.setvisita(False)
