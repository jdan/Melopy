#!/usr/bin/python

# generic parser for Melopy
#
#  $ python parser.py entertainer < examples/meeps/entertainer.mp

from melopy import *
from sys import argv, exit

if len(argv) < 2:
    fn = 'melody'
else:
    fn = argv[1]

m = Melopy(fn)
buff = raw_input()
data = buff

while True:
    try:
        buff = raw_input()
        data += '\n' + buff
    except EOFError:
        break

m.parse(data)
m.render()
