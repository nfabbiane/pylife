##############################################################################80
#                                                                              #
# UPDATE RULES                                                                 #
#                                                                              #
################################################################################




################################################################################
# Classic
#
def classic(cell, map, born=3, die=4, alone=1):
	"""
	cell_n+1 = classic(cell_n, map_n, born=3, die=4, alone=1)
	"""
	# evaluate environment
	env=0
	for id in cell.neighbours:
		env+=map.cells[id].state
	# apply rules
	oldstate=cell.state
	if cell.state==0:
		cell.age=0
		if env==born: cell.state=1
	else:
		cell.age+=1
		if env>=die: cell.state=0
		if env<=alone: cell.state=0
	return cell
