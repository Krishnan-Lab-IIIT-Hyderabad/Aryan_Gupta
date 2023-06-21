import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('./src')
import Box
import Propagator
from Thermostats import Anderson, Berendsen, Velocity_rescale, Non
from Energy import pe_sys,F
from Minimisation import minisation



# Set up for box 
particles = Box.createBox(2,6)  # n,L
sim = Propagator.createSim(300, 0.01) # s, t



# Calculate some sigma for Anderson, sigma = square root of KbT
sim.sigma = 0.1*np.sqrt((pe_sys(particles.X)*2)/9)
sim.nu = 7
# Berendsen & Velocity rescale, constant temp T lets assume the KE & tau for Berendsen 
sim.ke_T = pe_sys(particles.X)/4.5
sim.tau = 10*sim.t


# Run Minimisation 
j,pefound = minisation(sim,particles)

# Run simulation 
sim.run(particles,Non)

print("minimisation pe found: ", pefound)
print("actual min pe:", np.min(sim.PE))
sim.plotMin((j-1)/sim.s,pefound)

#sim.plot0th()