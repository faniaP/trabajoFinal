#! /usr/bin/python
# -*- coding: utf-8 _*_
from readXML import *

######################################
# Clase acciones es la que se encarga#
# de reforzar, atacar-defender y	 #
# conquistar los territorios.		 #
# E. Antonio Galvan Gamez			 #
# Fernando A. Galicia Mendoza		 #
# Estefania Prieto Larios			 #
######################################		

class acciones:


	territorio1 = territorio()

	'''Ganancia de tropas'''

	def gananciatropas(self,jugador):
		for jugador1 in territorio.getpaises(jugador):
			i = sum(jugador1.findall('nombre'))
			print i
			print jugador1





	''' Refuerza el pais como funcion'''
	
	'''def reforzar(self,pais_r,tropas):'''
	


			

	
	''' Ataca-Defiende'''
