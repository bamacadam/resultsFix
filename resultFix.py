import sympy as sp
import numpy as np
import itertools as it
import json

solns = json.load(open("data1.json", "r"))

"""
Generate matrices
"""

#Generate parities
singleParities = tuple(it.product([-1,1], repeat=7))
pars = tuple(it.product(singleParities, repeat=2))
#apply parity
def appPair(x,y):
    return lambda x,y : tuple(
        (i*j[0], i*j[1]) for (i,j) in it.product(x,y)
        )

def appParPair(uvst, parPair):
    return {'u':uvst['u'].copy(), 's':uvst['s'].copy()
            'v':appPair(parPair[0], uvst['v']),
            't' : appPair(parPair[0], uvst['t'])}
    
#generate Matrix

def tensor(x,y):
    return tuple(
    i*j for (i,j) in it.product(x,y)
    )

def matGen(uvst):
    left = tuple(i ++ j for (i,j) in zip(uvst['u'], uvst['v']))    
    right = tuple(i ++ j for (i,j) in zip(uvst['s'], uvst['t'])) 
    return sp.Matrix(
        list(tensor(i,j) for (i,j) in zip(left, right))
        ).transpose()

def genListEntries(uvst):
    for i in pars:
        yield matGen(appParPair(uvst,i))

def genList(uvst):
    return list(genListEntries(uvst))
    
