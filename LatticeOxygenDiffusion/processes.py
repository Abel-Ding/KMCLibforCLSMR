# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 11:12:34 2017

@author: abel
"""

from KMCLib import *
import numpy as np

#describe the interactions with custom rate calculator, 6 process, and oxygen jump

#Oxygen vacancy jump
elements_before = ["V","O"]
elements_after = ["O","V"]

#only on oxygen sites
basis_sites = [0]

#flow down in Z-axis
rate_constant_up = 0.9
rate_constant_down = 1.1

#all other rates
rate_constant = 1.0

#fill the list of processes
processes = []

#right
coordinates = [[0.000000e+00,0.000000e+00,0.000000e+00,],
               [1.000000e+00,0.000000e+00,0.000000e+00,]]
processes.append(KMCProcess(coordinates=coordinates,
                            elements_before=elements_before,
                            elements_after=elements_after,
                            basis_sites=basis_sites,
                            rate_constant=rate_constant))

#left
coordinates = [[0.000000e+00,0.000000e+00,0.000000e+00,],
               [-1.000000e+00,0.000000e+00,0.000000e+00,]]
processes.append(KMCProcess(coordinates=coordinates,
                            elements_before=elements_before,
                            elements_after=elements_after,
                            basis_sites=basis_sites,
                            rate_constant=rate_constant))
                            
#forward
coordinates = [[0.000000e+00,0.000000e+00,0.000000e+00,],
               [0.000000e+00,1.000000e+00,0.000000e+00,]]
processes.append(KMCProcess(coordinates=coordinates,
                            elements_before=elements_before,
                            elements_after=elements_after,
                            basis_sites=basis_sites,
                            rate_constant=rate_constant))

#back
coordinates = [[0.000000e+00,0.000000e+00,0.000000e+00,],
               [0.000000e+00,-1.000000e+00,0.000000e+00,]]
processes.append(KMCProcess(coordinates=coordinates,
                            elements_before=elements_before,
                            elements_after=elements_after,
                            basis_sites=basis_sites,
                            rate_constant=rate_constant))

#up
coordinates = [[0.000000e+00,0.000000e+00,0.000000e+00,],
               [0.000000e+00,0.000000e+00,1.000000e+00,]]
processes.append(KMCProcess(coordinates=coordinates,
                            elements_before=elements_before,
                            elements_after=elements_after,
                            basis_sites=basis_sites,
                            rate_constant=rate_constant_up))
                            
#down
coordinates = [[0.000000e+00,0.000000e+00,0.000000e+00,],
               [0.000000e+00,0.000000e+00,-1.000000e+00,]]
processes.append(KMCProcess(coordinates=coordinates,
                            elements_before=elements_before,
                            elements_after=elements_after,
                            basis_sites=basis_sites,
                            rate_constant=rate_constant_down))

#the final interactions object 隐式通配符
interactions = KMCInteractions(processes=processes, implicit_wildcards=True)
