##############################################################################80
#                                                                              #
# RANDOM INITIAL CONDITION WITH PERIODIC BOUNDARY CONDITIONS                   #
#                                                                              #
################################################################################
import sys
import os

# add library dir to path
pwd=os.path.dirname(os.path.abspath(__file__))
sys.path.append(pwd+"/../")

# import life library
import life




################################################################################
# Parameters
#
shape = [10, 20]
bc    = ["periodic", "periodic"]
steps = 200

# visualisation
fps = 30




################################################################################
# Example 
#
# initialize map
map = life.map(shape=shape, bc=bc)
# initialize plot
plt = life.plot.lite(); plt.open()
# random initial condition
map.rand()
plt.plot(map)
# step state and plot
for i in range(steps):
	map.step()
	plt.plot(map, step=i+1, wait=1./fps)
# close plot session
plt.close()
