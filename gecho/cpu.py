"""
Will Dignazio
gecho 2013
"""

class ProcCPUEntry(object):
	""" /proc/stat CPU Entry """
	def __init__(self, user, niced, system, idle, iowait, irq, softirq):
		self.user = user	# User processes
		self.niced = niced	# Processes under niced
		self.system = system# System (kernel) processes
		self.idle = idle	# Idling
		self.iowait = iowait# Waiting for I/O complete
		self.irq = irq		# Servicing interrupts
		self.softirq = softirq	# Servicing softirq's
