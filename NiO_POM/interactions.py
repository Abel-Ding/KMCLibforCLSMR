#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 00:20:43 2018

@author: abel
"""

#the process in KMC sim


from KMCLib import *

coordinates = [[   0.000000e+00,   0.000000e+00,   0.000000e+00]]
T = 873
e = 2.718281828
R=8.3145
P=6000.0
P_CH4 = P*0.5

#define the k based on pre-exponential factor, activation energy, gas constant and temperature
def RateCalculator(A, Ea, T=873):
    R = 8.3145
    e = 2.718281828
    k = A * (e**(-1*Ea/(R*T)))
    return k

# define the k of diffusion
D_Oi = 5.45E-7
a = 2.48E-10
Qi = 158679.72
K_diff = D_Oi/a/a * (e**(-1*Qi/R/T))

#coordinates four direction  wait for confirm
coordinate_right = [[   0.000000e+00,   0.000000e+00,   0.000000e+00],
                    [   1.000000e+00,   0.000000e+00,   0.000000e+00]]

coordinate_left = [[   0.000000e+00,   0.000000e+00,   0.000000e+00],
                    [   -1.000000e+00,   0.000000e+00,   0.000000e+00]]

coordinate_up = [[   0.000000e+00,   0.000000e+00,   0.000000e+00],
                    [   0.000000e+00,   1.000000e+00,   0.000000e+00]]

coordinate_down = [[   0.000000e+00,   0.000000e+00,   0.000000e+00],
                    [   0.000000e+00,   -1.000000e+00,   0.000000e+00]]

# for signle-cell adsprption/desorption
coordinate_single = [[   0.000000e+00,   0.000000e+00,   0.000000e+00]]


process = []

#1 CH4+E=>CH4*
process.append(KMCProcess(coordinates=coordinate_single,
                          elements_before = ['E'],
                          elements_after= ['CH4*'],
                          basis_sites = [0],
                          rate_constant = 0.0045*P_CH4))

#2 CH4*=>CH4+E
process.append(KMCProcess(coordinates=coordinate_single,
                          elements_before = ['CH4*'],
                          elements_after = ['E'],
                          basis_sites = [0],
                          rate_constant = RateCalculator(1.0E4, 33075.72, T))) 

#3 CH4*+* => CH3*+H*
for coordinates in [coordinate_right, coordinate_left, coordinate_up, coordinate_down]:
    process.append(KMCProcess(coordinates=coordinates,
                              elements_before = ['CH4*','E'],
                              elements_after =  ['CH3*','H*'],
                              basis_sites = [0],
                              rate_constant = RateCalculator(1.3E8, 57777.84,T))) 
    
#4 CH3*+E => CH2*+H*
for coordinates in [coordinate_right, coordinate_left, coordinate_up, coordinate_down]:
    process.append(KMCProcess(coordinates=coordinates,
                              elements_before = ['CH3*','E'],
                              elements_after =  ['CH2*','H*'],
                              basis_sites = [0],
                              rate_constant = RateCalculator(1.0E13, 115555.68, T)))
    
#5 CH2*+E=>CH*+H*
for coordinates in [coordinate_right, coordinate_left, coordinate_up, coordinate_down]:
    process.append(KMCProcess(coordinates=coordinates,
                              elements_before = ['CH2*','E'],
                              elements_after =  ['CH*','H*'],
                              basis_sites = [0],
                              rate_constant = RateCalculator(1.0E13, 97133.76, T))) 
    
#6 CH*+E=>C*+H*
for coordinates in [coordinate_right, coordinate_left, coordinate_up, coordinate_down]:
    process.append(KMCProcess(coordinates=coordinates,
                              elements_before = ['CH*','E'],
                              elements_after =  ['C*','H*'],
                              basis_sites = [0],
                              rate_constant = RateCalculator(1.0E13, 18840.6))) 
    
#7 O2+2E => 2O*
for coordinates in [coordinate_right, coordinate_left, coordinate_up, coordinate_down]:
    process.append(KMCProcess(coordinates=coordinates,
                              elements_before = ['E','E'],
                              elements_after =  ['O*','O*'],
                              basis_sites = [0],
                              rate_constant = 33*(P-P_CH4))) 
    
#8 2O*=> O2+2E
for coordinates in [coordinate_right, coordinate_left, coordinate_up, coordinate_down]:
    process.append(KMCProcess(coordinates=coordinates,
                              elements_before = ['O*','O*'],
                              elements_after =  ['E','E'],
                              basis_sites = [0],
                              rate_constant = RateCalculator(1.0E11, 186731.28, T))) 
    
#9 C*+O*=>CO*+E*
for coordinates in [coordinate_right, coordinate_left, coordinate_up, coordinate_down]:
    process.append(KMCProcess(coordinates=coordinates,
                              elements_before = ['C*','O*'],
                              elements_after =  ['CO*','E'],
                              basis_sites = [0],
                              rate_constant = RateCalculator(1.0E12, 146538, T))) 
    
#10 CO*=>CO+E
process.append(KMCProcess(coordinates=coordinate_single,
                          elements_before = ['CO*'],
                          elements_after =  ['E'],
                          basis_sites = [0],
                          rate_constant = RateCalculator(1.0E10, 116602.38, T))) 

#11 2H*=>H2+2E
for coordinates in [coordinate_right, coordinate_left, coordinate_up, coordinate_down]:
    process.append(KMCProcess(coordinates=coordinates,
                              elements_before = ['H*','H*'],
                              elements_after =  ['E','E'],
                              basis_sites = [0],
                              rate_constant = RateCalculator(3.1E12, 97552.44, T))) 
    
#12 CO*+O*=>CO2+2E
for coordinates in [coordinate_right, coordinate_left, coordinate_up, coordinate_down]:
    process.append(KMCProcess(coordinates=coordinates,
                              elements_before = ['CO*','O*'],
                              elements_after =  ['E', 'E'],
                              basis_sites = [0],
                              rate_constant = RateCalculator(5.0E6, 63639.36, T))) 
    
#13 H*+O*=>OH*+E
for coordinates in [coordinate_right, coordinate_left, coordinate_up, coordinate_down]:
    process.append(KMCProcess(coordinates=coordinates,
                              elements_before = ['H*','O*'],
                              elements_after =  ['OH*','E'],
                              basis_sites = [0],
                              rate_constant = RateCalculator(1.0E7, 82061.28, T))) 
    
#14 H*+OH*=>H2O+2E
for coordinates in [coordinate_right, coordinate_left, coordinate_up, coordinate_down]:
    process.append(KMCProcess(coordinates=coordinates,
                              elements_before = ['H*','OH*'],
                              elements_after =  ['E','E'],
                              basis_sites = [0],
                              rate_constant = RateCalculator(3.10E11, 32238.36, T))) 
    
#15 O*=>Ox
process.append(KMCProcess(coordinates=coordinate_single,
                          elements_before = ['O*'],
                          elements_after =  ['Ox'],
                          basis_sites = [0],
                          rate_constant = RateCalculator(1.0E5, 65732.76, T))) 

#16 C*+Ox=>CO*+E
for coordinates in [coordinate_right, coordinate_left, coordinate_up, coordinate_down]:
    process.append(KMCProcess(coordinates=coordinates,
                              elements_before = ['C*','Ox'],
                              elements_after =  ['CO*','E'],
                              basis_sites = [0],
                              rate_constant = RateCalculator(1.0E7, 109861.632, T))) 
    
#17 CO*+Ox=>CO2+2E
for coordinates in [coordinate_right, coordinate_left, coordinate_up, coordinate_down]:
    process.append(KMCProcess(coordinates=coordinates,
                              elements_before = ['CO*','Ox'],
                              elements_after =  ['E','E'],
                              basis_sites = [0],
                              rate_constant = RateCalculator(1.0E5, 71175.6, T))) 
    
#18 H*+Ox=> OH*+E
for coordinates in [coordinate_right, coordinate_left, coordinate_up, coordinate_down]:
    process.append(KMCProcess(coordinates=coordinates,
                              elements_before = ['H*','Ox'],
                              elements_after =  ['OH*','E'],
                              basis_sites = [0],
                              rate_constant = RateCalculator(5.20E3, 46054.8, T))) 
    
#CH4* diffusion
for coordinates in [coordinate_right, coordinate_left, coordinate_up, coordinate_down]:
    process.append(KMCProcess(coordinates=coordinates,
                              elements_before = ['CH4*','E'],
                              elements_after =  ['E','CH4*'], 
                              basis_sites = [0],
                              rate_constant = K_diff))
    
#C* diffusion
for coordinates in [coordinate_right, coordinate_left, coordinate_up, coordinate_down]:
    process.append(KMCProcess(coordinates=coordinates,
                              elements_before = ['C*','E'],
                              elements_after =  ['E','C*'],
                              basis_sites = [0],
                              rate_constant = K_diff))
    
#H* diffusion
for coordinates in [coordinate_right, coordinate_left, coordinate_up, coordinate_down]:
    process.append(KMCProcess(coordinates=coordinates,
                              elements_before = ['H*','E'],
                              elements_after =  ['E','H*'],
                              basis_sites = [0],
                              rate_constant = K_diff))
    
#O* diffusion
for coordinates in [coordinate_right, coordinate_left, coordinate_up, coordinate_down]:
    process.append(KMCProcess(coordinates=coordinates,
                              elements_before = ['O*','E'],
                              elements_after =  ['E','O*'],
                              basis_sites = [0],
                              rate_constant = K_diff) )
    
#CO* diffusion
for coordinates in [coordinate_right, coordinate_left, coordinate_up, coordinate_down]:
    process.append(KMCProcess(coordinates=coordinates,
                              elements_before = ['CO*','E'],
                              elements_after =  ['E','CO*'],
                              basis_sites = [0],
                              rate_constant = K_diff))
    
#OH* diffusion
for coordinates in [coordinate_right, coordinate_left, coordinate_up, coordinate_down]:
    process.append(KMCProcess(coordinates=coordinates,
                              elements_before = ['OH*','E'],
                              elements_after =  ['E','OH*'],
                              basis_sites = [0],
                              rate_constant = K_diff))
    
#Ox diffusion
for coordinates in [coordinate_right, coordinate_left, coordinate_up, coordinate_down]:
    process.append(KMCProcess(coordinates=coordinates,
                              elements_before = ['Ox','E'],
                              elements_after =  ['E','Ox'],
                              basis_sites = [0],
                              rate_constant = K_diff))

interactions = KMCInteractions(
        processes=process,
        implicit_wildcards=True)
