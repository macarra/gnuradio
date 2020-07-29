#!/bin/env python3

import numpy as np
import sys

def GetBytesFromFile(filename):
    bytes = np.fromfile(filename,dtype= "uint8")
    return bytes

def viewbits(data,rows=0,cols=32):
    bits = np.unpackbits(bytes)
    if rows == 0: rows = len(bits)//cols
    for row in range(0,rows):
        bitstring=''
        for bit in bits[row*cols:row*cols+cols]: bitstring+=str(bit)
        print(bitstring)
    


if __name__ == '__main__':

    filename = 'testinput.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        
    cols = 32
    if len(sys.argv) > 2:
        cols = int(sys.argv[2])
        
    rows = 0
    if len(sys.argv) > 3:
        rows = int(sys.argv[3])
        

        
    bytes = GetBytesFromFile(filename)
        
    viewbits(bytes,rows,cols)
    
    exit()
