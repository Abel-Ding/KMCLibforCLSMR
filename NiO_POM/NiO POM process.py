#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 16:09:01 2018

@author: abel
"""

#NiO process

import time
from KMCLib import *
from matplotlib import pyplot as plt

t_calstart = time.clock()
configuration = KMCConfigurationFromScript("config.py")
interactions  = KMCInteractionsFromScript("interactions.py")

model = KMCLatticeModel(configuration=configuration, interactions=interactions)

control_parameters = KMCControlParameters(number_of_steps=10000000,
                                          dump_interval=10000)

# Run the simulation - save trajectory to 'NiO POM.py'
model.run(control_parameters, trajectory_filename="NiO POM.py")
t_calend = time.clock()
print("sim complete time cost is :", t_calend-t_calstart) 
#length of lattice
size = 100