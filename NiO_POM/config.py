# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from KMCLib import *
import numpy as np

#define the unit cell NiO 2.48E-10m  2.58A
cell_vectors = [[   2.480000e+00,   0.000000e+00,   0.000000e+00],
                [   0.000000e+00,   2.480000e+00,   0.000000e+00],
                [   0.000000e+00,   0.000000e+00,   2.480000e+00]]

basis_points = [[   0.000000e+00,   0.000000e+00,   0.000000e+00]]

unit_cell = KMCUnitCell(cell_vectors=cell_vectors,
                        basis_points=basis_points)

#define the lattice
lattice = KMCLattice(unit_cell=unit_cell,
                     repetitions=(100,100,1),
                     periodic=(True, True, False))

#generate the initial type
#E for empty, initial surface is empty 
types = ['E']*10000
    
#set up the configuration
configuration = KMCConfiguration(lattice = lattice,
                                 types=types,
                                 possible_types = ['E','CH4','CH4*', 'CH3*', 'CH2*', 'CH*', 'C*', 'H*', 'H2', 'O2', 'O*', 'Ox', 'CO', 'CO*', 'CO2', 'H2O' ])

#use the _script() function to get a script for generation of the config

print configuration._script()

    