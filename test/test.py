##############################################################################80
#                                                                              #
# TESTS FOR GAME OF LIFE LIBRARY                                               #
#                                                                              #
################################################################################
import sys
import os

# add library dir to path
pwd=os.path.dirname(os.path.abspath(__file__))
sys.path.append(pwd+"/../../")

# import life library
import pylife




################################################################################
# Define square steady solution check
#
def check_square(steps=10):
	# initialize
	map = pylife.map(shape=[3, 3])
	# steady state
	square=[[1, 1, 0],
			  [1, 1, 0],
			  [0, 0, 0]]
	# initialize state
	map.setstate(square)
	# - check
	passed=(square==map.getstate()).all()
	# step state
	for i in range(steps):
		map.step()
		# check steady state
		passed=passed&(square==map.getstate()).all()
	# output
	assert(passed)




################################################################################
# Define propeller periodic orbit check
#
def check_propeller(steps=10):
	# initialize
	map = pylife.map(shape=[3, 3])
	# states of the period 2 orbit
	propeller=[[[0, 0, 0],
					[1, 1, 1],
					[0, 0, 0]],
				  [[0, 1, 0],
					[0, 1, 0],
					[0, 1, 0]]]
	# initialize state
	map.setstate(propeller[0])
	# - check
	passed=(propeller[0]==map.getstate()).all()
	# step state
	for i in range(steps):
		map.step()
		# check periodic orbit
		passed=passed&(propeller[(i+1)%2]==map.getstate()).all()
	# output
	assert(passed)




################################################################################
# Define glider solution check
#
def test_glider(steps=20):
	# initialize
	map = pylife.map(shape=[5, 5], bc=["periodic", "periodic"])
	# initial state
	glider=[[1, 0, 0, 0, 0],
			  [0, 1, 1, 0, 0],
			  [1, 1, 0, 0, 0],
			  [0, 0, 0, 0, 0],
			  [0, 0, 0, 0, 0]]
	# initialize state
	map.setstate(glider)
	# - check
	passed=(glider==map.getstate()).all()
	# step state
	for i in range(0, steps):
		map.step()
		# check glider
		if (i+1)%20==0: passed=passed&(glider==map.getstate()).all()
	# output
	assert(passed)




################################################################################
# Define propeller periodic orbit check
#
def check_plot_lite(steps=10):
	# initialize
	map = pylife.map(shape=[3, 3])
	# initialize plot
	plt = pylife.plot.lite(); plt.open()
	# initialize state (random)
	map.rand()
	plt.plot(map, step=0)
	# step state
	for i in range(steps):
		map.step()
		plt.plot(map, step=i+1)
	# close plot session
	plt.close()




################################################################################
# run tests
#
if __name__ == "__main__":

	test_square()
	test_propeller()
	test_glider()
