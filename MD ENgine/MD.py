import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('./src')
import Box
import Propagator
from Thermostats import Anderson, Berendsen, Velocity_rescale, Non
from Energy import pe_sys



# Set up for box 
particles = Box.createBox(10,6)  # n,L
sim = Propagator.createSim(10000, 0.01) # s, t


# Calculate some sigma for Anderson, sigma = square root of KbT, let KE = PE/3 at T and KE = 3/2 KbT
sim.sigma = 0.1*np.sqrt((pe_sys(particles.X)*2)/9)
sim.nu = 7

# Berendsen & Velocity rescale, constant temp T lets assume the KE & tau for Berendsen 
sim.ke_T = pe_sys(particles.X)/4.5
sim.tau = 10*sim.t


# Run simulation 
sim.run(particles,Anderson)
sim.plot()
#sim.plot0th()