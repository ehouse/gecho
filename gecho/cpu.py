"""
Will Dignazio
gecho 2013
"""

import gecho
import time
import multiprocessing
from gecho.procfs import *

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

		self.procfs = gecho.procfs.procfs
	def __str__(self):
		return self.name + " " + self.user + " " + self.user + " " + self.niced\
			+ " " + self.system + " " + self.idle + " " + self.iowait + " " +\
			self.irq + " " + self.softirq

	@staticmethod
	def spawn_cpu_monitor(idle):
		""" Spawns A CPU Monitor, returns a reference to it """
		class CPU_MONITOR(object):
			""" CPU_Monitor object """
			def __init__(self):
				publishes = 0
				child = multiprocessing.Process(target=self.worker, args=(idle,))
				child.start()
			@staticmethod
			def notify_event(notifier):
				print "TEST"
			@staticmethod
			def worker(idle):
				""" Worker Process """
				while True:
					# Idle for the alloted time, will make the traffic sane. 
					time.sleep(idle)
					cpus = procfs.get_cpus()
					for cpu in cpus:
						print cpu
						#gechoQueue.put(cpu) #Enqueue the data for publishing
			def kill():
				""" Kills the child worker process """
				child.terminate()
		return CPU_MONITOR()

if __name__ == "__main__":
	m = ProcCPU.spawn_cpu_monitor(1)
