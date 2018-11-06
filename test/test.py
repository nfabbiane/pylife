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
def check_square(steps):
	# initialize
	map = pylife.map(shape=[3, 3])
	# initialize plot
	plt = pylife.plot.lite(); plt.open()
	# steady state
	square=[[1, 1, 0],
			  [1, 1, 0],
			  [0, 0, 0]]
	# initialize state
	map.setstate(square)
	plt.plot(map)
	# - check
	check=(square==map.getstate()).all()
	# step state
	for i in range(steps):
		map.step()
		plt.plot(map, step=i+1)
		# check steady state
		check=check&(square==map.getstate()).all()
	# close plot session
	plt.close()
	# output
	return check




################################################################################
# Define propeller periodic orbit check
#
def check_propeller(steps):
	# initialize
	map = pylife.map(shape=[3, 3])
	# initialize plot
	plt = pylife.plot.lite(); plt.open()
	# states of the period 2 orbit
	propeller=[[[0, 0, 0],
					[1, 1, 1],
					[0, 0, 0]],
				  [[0, 1, 0],
					[0, 1, 0],
					[0, 1, 0]]]
	# initialize state
	map.setstate(propeller[0])
	plt.plot(map)
	# - check
	check=(propeller[0]==map.getstate()).all()
	# step state
	for i in range(steps):
		map.step()
		plt.plot(map, step=i+1)
		# check periodic orbit
		check=check&(propeller[(i+1)%2]==map.getstate()).all()
	# close plot session
	plt.close()
	# output
	return check




################################################################################
# Define glider solution check
#
def check_glider(steps):
	# initialize
	map = pylife.map(shape=[5, 5], bc=["periodic", "periodic"])
	# initialize plot
	plt = pylife.plot.lite(); plt.open()
	# initial state
	glider=[[1, 0, 0, 0, 0],
			  [0, 1, 1, 0, 0],
			  [1, 1, 0, 0, 0],
			  [0, 0, 0, 0, 0],
			  [0, 0, 0, 0, 0]]
	# initialize state
	map.setstate(glider)
	plt.plot(map)
	# - check
	check=(glider==map.getstate()).all()
	# step state
	for i in range(0, steps):
		map.step()
		plt.plot(map, step=i+1)
		# check glider
		if (i+1)%20==0: check=check&(glider==map.getstate()).all()
	# close plot session
	plt.close()
	# output
	return check




################################################################################
# run tests
#
assert(check_square(10))
assert(check_propeller(10))
assert(check_glider(20))
