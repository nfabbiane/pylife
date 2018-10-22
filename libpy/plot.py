##############################################################################80
#                                                                              #
# PLOT UTILS                                                                   #
#                                                                              #
################################################################################




################################################################################
# Lite
#
class lite:
	def open(self):
		"""
		opens a terminal based plot
		"""
		import curses
		# initialize
		self.stdscr=curses.initscr()
	#
	#----------------------------------------------------------------------------
	def plot(self, map, wait=0.1, step=None):
		"""
		plot(map, wait=0.1, step=None)
		
		terminal based plot
		"""
		import time
		# state
		for i in range(map.shape[0]):
			for j in range(map.shape[1]):
				if map.cells[(i,j)].state>0: cell="#"
				else: cell= " "
				self.stdscr.addstr(i+2, j+2, cell)
		# frame
		self.stdscr.addstr(2, 0, "i")
		self.stdscr.addstr(0, 2, "j")
		self.stdscr.addstr(1, 1, "+"+"-"*map.shape[1]+">")
		for i in range(map.shape[0]):
			self.stdscr.addstr(i+2, 1, "|")
			self.stdscr.addstr(i+2, map.shape[1]+2, "|")
		self.stdscr.addstr(map.shape[0]+2, 1, "v"+"-"*map.shape[1]+"+")
		# step
		if isinstance(step, int):
			self.stdscr.addstr(map.shape[0]+4, 1, "step: %d" %(step))
		# output
		self.stdscr.refresh()
		time.sleep(wait)
	#
	#----------------------------------------------------------------------------
	def close(self):
		"""
		closes a terminal based plot
		"""
		import curses
		# initialize
		curses.endwin()
	



################################################################################
# Full (with matplotlib)
#
class full:
	def open(self, shape=[1., 1.], border=0):
		"""
		opens a matplotlib based plot
		"""
		import numpy as np
		import matplotlib.pyplot as plt
		# initialize figure and axis
		figsize=np.flip(shape)/float(np.max(shape))*5.
		self.fig=plt.figure(figsize=figsize)
		#initialize axis
		position=[border, border, 1.-2*border, 1.-2*border]
		self.ax=plt.axes(position=position)
		self.ax.axis('off')
		# snapshot array
		self.snaps=[]
	#
	#----------------------------------------------------------------------------
	def plot(self, map, wait=0.1, step=None, show=False):
		"""
		plot(map, wait=0.1, step=None)
		
		matplotlib based plot
		"""
		import matplotlib.pyplot as plt
		import time
		# plot state
		state=map.getstate()
		snap=self.ax.imshow(state, cmap='Greys', animated=True)
		# collect snapshot
		self.snaps.append([snap])
		# show
		if show:
			plt.show(block=False)
			# wait
			time.sleep(wait)
	#
   #----------------------------------------------------------------------------
	def close(self, fps=0):
		"""
		closes a matplotlib based plot and saves animated gif if fps>0
		"""
		if fps>0:
			import matplotlib.animation as anm
			# create animation
			ani=anm.ArtistAnimation(self.fig, self.snaps)
			# get filename
			import sys
			import os
			filename=os.path.splitext(sys.argv[0])[0]+".gif"
			# save animation
			ani.save(filename, writer='imagemagick', fps=fps,
						savefig_kwargs={'bbox_inches': 'tight', 'pad_inches': 0})
		# close figure
		import matplotlib.pyplot as plt
		plt.close(self.fig)
	
