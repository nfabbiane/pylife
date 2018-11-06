##############################################################################80
#                                                                              #
# CLASSES DEFINITION                                                           #
#                                                                              #
################################################################################
import rules




################################################################################
# Cell definition
#
class cell:
	def __init__(self, state=0, neighbours=[], age=0):
		"""
		initialize cell
		
		.state=0
		.neighbours=[]
		.age=0
		"""
		self.state=state
		self.neighbours=[]
		self.age=age




################################################################################
# 2D Map definition
#
class map:
	def __init__(self, shape=(2, 2), bc=[None, None]):
		"""
		initialize a map
		
		.shape=(2, 2)
		.cells=<list of cells {(i,j): cell}>
		
		cell state is initilize to 0; use .rand() to initialize with random
		values.
		
		boundary conditions are given by the optional input bc; see .setbc() for
		the boundary conditions available
		"""
		# shape
		self.shape=tuple(shape)
		# create map
		self.cells={}
		for i in range(self.shape[0]):
			for j in range(self.shape[1]):
				self.cells[(i,j)]=cell(state=0);
		# set boundary conditions
		self.setbc(bc=bc)
		# check map
		#self.check()
   #
   #----------------------------------------------------------------------------
	def setbc(self, bc=["periodic", "periodic"]):
		"""
		set boundary conditions
		
		input: bc=[bci, bcj]
		
		The values bci and bcj prescribe the boundary conditions in the i and j
		direction respectively
		These two string variables can take the values:
		
		- "cliff" (or None): cliff boundary condition, i.e. no life out of the box
		- "periodic":        periodic boundary condition
		- "symmetric":       symmetry boundary conditions
		
		Any other value will fall in the "cliff" case.
		"""
		# check inputs
		bca=["cliff", "periodic", "symmetric"]
		for i in range(len(bc)):
			if isinstance(bc[i], str): 
				if not(bc[i] in bca):
					print ("WARNING! bc '%s' not implemented: '%s' used instead."
							 %(bc[i], bca[0]))
					bc[i]=bca[0]
			else: bc[i]=bca[0]
		# cycle on cells
		for (id, cell) in self.cells.iteritems():
			# cycle on neighbours
			for ii in range(id[0]-1, id[0]+2):
				for jj in range(id[1]-1, id[1]+2):
					if (ii,jj)!=id:
						# i boundary conditions
						if "periodic" in bc[0]: ii=ii%self.shape[0]
						if "symmetric" in bc[0]:
							if (ii<0)|(self.shape[0]<=ii):
								ii=(self.shape[0]-ii)%self.shape[0]
						# j boundary conditions
						if "periodic" in bc[1]: jj=jj%self.shape[1]
						if "symmetric" in bc[1]:
							if (jj<0)|(self.shape[1]<=jj): jj=(-jj)%self.shape[1]
						# add neighbour
						idn=(ii,jj)
						if idn in self.cells.keys():
							cell.neighbours.append(idn)
   #
   #----------------------------------------------------------------------------
	def rand(self):
		"""
		set state to random value
		"""
		import numpy as np
		# cycle on cells
		for (id, cell) in self.cells.iteritems():
			cell.state=np.random.randint(2)
   #
   #----------------------------------------------------------------------------
	def getstate(self):
		"""
		returns the state for each cell of the map
		"""
		import numpy as np
		# initialize state 2D array
		state=np.zeros(self.shape)
		# cycle on cells
		for (id, cell) in self.cells.iteritems():
			state[id[0], id[1]]=cell.state
		# output
		return state
   #
   #----------------------------------------------------------------------------
	def setstate(self, state):
		"""
		set the state for each cell of the map
		"""
		import numpy as np
		# check given state
		state=np.array(state)
		shape=state.shape
		if (shape[0]>self.shape[0]) & (shape[1]>self.shape[1]):
			print ("WARNING! state.shape = (%d, %d)" %state.shape+
					 " != (%d, %d) = map.shape" %self.shape)
			return
		# cycle on cells
		for (id, cell) in self.cells.iteritems():
			if (id[0]<shape[0]) & (id[1]<shape[1]):
				cell.state=state[id[0], id[1]]
   #
   #----------------------------------------------------------------------------
	def getage(self):
		"""
		returns the age for each cell of the map
		"""
		import numpy as np
		# initialize state 2D array
		age=np.zeros(self.shape)
		# cycle on cells
		for (id, cell) in self.cells.iteritems():
			age[id[0], id[1]]=cell.age
		# output
		return age
   #
   #----------------------------------------------------------------------------
	def step(self, rule=rules.classic):
		"""
		step map with rule(=rules.classic)
		"""
		import copy as cp
		# store current map
		curmap=cp.deepcopy(self)
		# apply rule to each cell
		for (id, cell) in self.cells.iteritems():
			cell=rule(cell, curmap)
