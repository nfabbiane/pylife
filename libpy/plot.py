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
    #---------------------------------------------------------------------------
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
    #---------------------------------------------------------------------------
	def close(self):
		"""
		closes a terminal based plot
		"""
		import curses
		# initialize
		curses.endwin()
	
