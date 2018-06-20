# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 10:24:08 2017

@author: abel
"""

from KMCLib import *
import numpy as np

#unit cell
cell_vectors = [[   2.782000e+00,   0.000000e+00,   0.000000e+00],
                [   0.000000e+00,   2.782000e+00,   0.000000e+00],
                [   0.000000e+00,   0.000000e+00,   2.782000e+00]]

basis_points = [[   0.000000e+00,   0.000000e+00,   0.000000e+00],
                [   5.000000e-01,   5.000000e-01,   5.000000e-01]]

unit_cell = KMCUnitCell(cell_vectors=cell_vectors,basis_points=basis_points)

#lattice
lattice = KMCLattice(unit_cell=unit_cell,
                     repetitions=(20,20,20),
                     periodic=(False,True,True))
                     
# O for oxygen, V for vacancy, M for metal,  E for empty
#loop over all cells, add the oxygen and metal
size = 20
types = []
for i in range(size):
    for j in range(size):
        for k in range(size):
            if k%2 == 0:
                if (i+j)%2 == 0:
                    types += ["O","M"]
                else:
                    types += ["O","E"]
            else:
                if (i+j+1)%2 == 0:
                    types += ["O","M"]
                else:
                    types += ["O","E"]

# add 3200 randomly positioned vacancies in the oxygen sub lattice
n_vacancies = 3200
defects = 0
while(defects<n_vacancies):
    position = int(np.random.uniform(0.0,1.0)*len(types))
    
    #make sure to repalce oxygen sites
    while(types[position] != "O"):
        position=int(np.random.uniform(0.0,1.0)*len(types))
    
    #replace with a vacancy
    types[position] = "V"
    defects += 1
    
#add 1600 dopants in the metal sites
n_dopants = 1600
dopants = 0
while(dopants < n_dopants):
    position=int(np.random.uniform(0.0, 1.0)*len(types))
    
    #make sure to replace metal sites
    while(types[position] != "M"):
        position = int(np.random.uniform(0.0, 1.0)*len(types))
        
    #repalce with a dopant
    types[position] = "D"
    dopants += 1
        
config = KMCConfiguration(lattice=lattice,
                          types=types,
                          possible_types=["E","M","D","O","V"])

