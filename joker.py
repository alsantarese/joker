#!/bin/python
from os import *

#####   color
r='\033[1;31m'
g='\033[1;32m'
y='\033[1;33m'
b='\033[1;34m'
p='\033[1;35m'
c='\033[1;36m'
w='\033[1;37m'
##############

system('clear')
system('toilet -f mono12 -F gay Joker')
print g + "[" + y + "1" + g + "]" + c + " Hack 010" + w + "		       Joker V 1.0"
print g + "[" + y + "2" + g + "]" + c + " Hack 012"
print g + "[" + y + "3" + g + "]" + c + " Hack 011" + g + "		  [" + y + "0" + g + "]" + r + " ExIT"
print g + "[" + y + "4" + g + "]" + c + " Hack 015"
print " "+ r
joker = input('         Enter Number~# ' + g)


if joker == 1:
	system('clear')
	print r
	system('figlet -f big  Vodafone')
	system('python2 .0100.py')
if joker == 2:
        system('clear')
	print y
	system('figlet -f mono12  Orange')
	system('python2 .0122.py')
if joker == 3:
        system('clear')
	print g
	system('figlet -f mono9 Etsalat')
	system('python2 .0111.py')
if joker == 4:
        system('clear')
	print p
	system('figlet -f mono12 W E')
	system('python2 .0155.py')
if joker == 0:
        system('clear')
        print r + " ........ Thanks Frind ........" + g + "   ^_^"
	system('exit')
