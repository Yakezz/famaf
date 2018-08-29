#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  TP 2.py
#  
#  Copyright 2018 Live System User <liveuser@localhost>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


from turtle import *
#Calle 1
def calles():
	for lados_Cant in range (3):
		for lados_C in range (4):
			right(90)
			forward(50)
					
					
					
		for lados_T in range (2):							
			left(360/3)
			forward(50)
		left(360/3)
		forward(100)
#Interseccion de las calles
def interseccion():
	left(90)
	forward(50)
	left(90)
	forward(200)
	right(90)
	forward(50)
	right(90)

#Primera calle		
calles()

#Interseccion de las calles
interseccion()

#Calle 2
calles()

exitonclick()
