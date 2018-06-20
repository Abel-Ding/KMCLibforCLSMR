# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 11:26:23 2017

@author: abel
"""

from KMCLib import *
import numpy as np
import os

#msd setup
msd_analysis = OnTheFlyMSD(history_steps=200, 
                           n_bins=100, 
                           t_max=100.0, 
                           track_type="V")

control_parameters = KMCControlParameters(number_of_steps=3000000,
                                          dump_interval=10000,
                                          analysis_interval=1,
                                          seed=1994669)

#run the model
directory = os.path.abspath(os.path.dirname(__file__))
p_file    = os.path.join(directory, "processes.py")
c_file    = os.path.join(directory,"config.py")
interactions  = KMCInteractionsFromScript(p_file)
configuration = KMCConfigurationFromScript(c_file)

model = KMCLatticeModel(configuration, interactions)
model.run(control_parameters,trajectory_filename="traj.py",analysis=[msd_analysis])

with open('msd.data', 'w') as f:
    msd_analysis.printResults(f)

with open('msd.data', 'r') as f:
    content = f.readlines()
raw_data = []

for row in content[1:]:
    row = [float(r) for r in row.split('\n')[0].split(' ') if r != '']
    raw_data.append(row)

raw_data = np.array(raw_data)

#data for plot
time = raw_data[:,0]
msd = raw_data[:,1]
std = raw_data[:,8]

import matplotlib.pyplot as plt

plt.figure(1)
ax1 = plt.subplot(111)
plt.plot(time, msd)
plt.plot(time,std)

plt.show()