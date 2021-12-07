import numpy as np
from tabulate import tabulate

DATI = {'A':[1,1,1,1,0,0,0,0], 'B':[1,0,1,0,1,0,1,0], 'C':[1,0,0,0,1,0,0,0]}
A,B,C = DATI['A'],DATI['B'],DATI['C']
def NOT(X): return np.logical_not(X)
def AND(X,Y): return np.logical_and(X,Y)
def OR(X,Y):  return np.logical_or(X,Y)


'''
DATI['A1'] = NOT(OR(NOT(A), AND(C, OR(NOT(B), A))))
DATI['A2'] = AND(A, OR(NOT(C), AND(B, NOT(A))))
DATI['A3'] = OR(AND(A,NOT(C)), AND(A,AND(B,NOT(A))))
DATI['A4'] = AND(A,NOT(C))
DATI['B1'] = AND(B,NOT(OR(A,AND(NOT(B), NOT(C)))))
DATI['B2'] = OR(AND(B,AND(NOT(A),B)), AND(B,AND(NOT(A), C)))
DATI['C1'] = AND(AND(A,NOT(C)), AND(A,NOT(C)))
DATI['C2'] = AND(A,NOT(C))
DATI['B3'] = AND(NOT(A), B)

DATI['E1'] = AND(AND(B,NOT(A)), B)
DATI['E2'] = AND(AND(NOT(A),B), B)
DATI['E3'] = AND(NOT(A), B)
'''

DATI['A1'] = OR(AND(OR(A,B), AND(A, NOT(B))), AND(B, NOT(A)))
DATI['A2'] = OR(AND(A,NOT(B)), AND(B, NOT(A)))
DATI['B1'] = NOT(OR(NOT(A), AND(OR(B,NOT(A)), NOT(B))))
DATI['B2'] = OR(AND(A,NOT(B)), AND(A,B))

DATI['S1'] = OR(A,AND(B,NOT(A)))
DATI['S'] = OR(A,B)
#DATI['D2'] = OR(AND(A,NOT(C)), AND(NOT(A), B))
print(tabulate(DATI, headers='keys'))