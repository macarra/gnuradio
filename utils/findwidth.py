#!/bin/env python3

import numpy as np
import sys

def GetBytesFromFile(filename):
    bytes = np.fromfile(filename,dtype= "uint8")
    return bytes

def findwidth(bytes,minwidth=8):
    bits = np.unpackbits(bytes)
    if minwidth < 2: minwidth=2
    width=minwidth
    maxwidth = len(bytes)//2
    while width < maxwidth:
        if bits[0:width] == bits[width:2*width]:
            return width
    return False
        

if __name__ == '__main__':

    filename = 'testinput.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        
    minwidth=8
    if len(sys.argv) > 2:
        minwidth = int(sys.argv[2])
        
    bytes = GetBytesFromFile(filename)
        
    foundwidth = findwidth(bytes,minwidth)
    if foundwidth:
        print("found width",foundwidth)
    
    exit()
