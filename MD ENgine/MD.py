import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('./src')
import Box
import Propagator
from Thermostats import Anderson, Berendsen, Velocity_rescale, Non
from Energy import pe_sys
from Minimisation import minisation



# Set up for box 
particles = Box.createBox(7,6)  # n,L
sim = Propagator.createSim(10000, 0.01) # s, t



# Calculate some sigma for Anderson, sigma = square root of KbT
sim.sigma = 0.1*np.sqrt((pe_sys(particles.X)*2)/9)
sim.nu = 7
# Berendsen & Velocity rescale, constant temp T lets assume the KE & tau for Berendsen 
sim.ke_T = pe_sys(particles.X)/4.5
sim.tau = 10*sim.t



# Run Minimisation 
minisation(sim,particles)
pefound = pe_sys(particles.X)

# Run simulation 
sim.run(particles,Non)
print("minimisation pe found: ", pefound)
print("actual min pe:", np.min(sim.PE))
sim.plot()
#sim.plot0th()