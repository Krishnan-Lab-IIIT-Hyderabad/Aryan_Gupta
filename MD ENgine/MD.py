# Still not able to debug 


import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('./src')
import Box
import Propagator
from Thermostats import Anderson, Velocity_rescale, Berendsen



# Set up for box 
particles = Box.createBox(10,6)  # n,L
sim = Propagator.createSim(10000, 0.01) # s, t

# Run simulation 
sim.run(particles,Anderson)


#sim.plot()

#x1 = np.linspace(0, 1, sim.s)
#plt.plot(x1, sim.H,color='green')
#plt.plot(x1, sim.PE,color='purple')
#plt.plot(x1, sim.KE, color='red')  


print(sim.H)