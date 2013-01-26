"""
Will Dignazio
gecho 2013
"""

import time
import thread
import gecho
from gecho.procfs import *
from gecho import GechoGlobal


class ProcCPU(object):
	""" /proc/stat CPU Entry """
	def __init__(self, name, user, niced, system, idle, iowait, irq, softirq):
		self.subscription = "CPU"
		self.name = name
		self.user = user	# User processes
		self.niced = niced	# Processes under niced
		self.system = system# System (kernel) processes
		self.idle = idle	# Idling
		self.iowait = iowait# Waiting for I/O complete
		self.irq = irq		# Servicing interrupts
		self.softirq = softirq	# Servicing softirq's
	def __str__(self):
		return self.name + " " + self.user + " " + self.user + " " + self.niced\
			+ " " + self.system + " " + self.idle + " " + self.iowait + " " +\
			self.irq + " " + self.softirq

	@staticmethod
	def spawn_cpu_monitor(idle):
		""" Spawns A CPU Monitor, returns a reference to it.
			Originally multiprocessing based, however this created
			more problems than solutions; our problem is IO bound,
			and separating instances will not alleviate this.
		"""
		def work():
			""" TODO: Add stop logic """
			while GechoGlobal.cpu_monitor_active:
				time.sleep(GechoGlobal.cpu_monitor_idle)
				for cpu in gecho.procfs.get_cpus():
					GechoGlobal.gechoQueue.put(cpu)
		try:
			if GechoGlobal.cpu_monitor_active == False:
				thread.start_new_thread(work,())
				GechoGlobal.cpu_monitor_active = True
			else:
				GechoGlobal.cpu_idle_time = idle
		except Exception as E:
			print "Unable to start CPU worker thread: %s", E


if __name__ == "__main__":
	ProcCPU.spawn_cpu_monitor(1)
	while True:
		pass
