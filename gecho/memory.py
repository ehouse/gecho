"""
Will Dignazio
gecho 2013
"""

import thread
import time
from gecho import GechoGlobal
import gecho.procfs

class ProcMem(object):
	""" Entry in /proc/meminfo """
	def __init__(self, value, memkb):
		self.subscription = "MEM"
		self.value = value
		self.memkb = memkb

	def megabytes(self):
		return self.memkb / 1024

	def __str__(self):
		return self.value + ": " + self.memkb

	@staticmethod
	def spawn_memory_monitor(idle):
		"""
			Spawns the Memory Monitor to monitor the fields of
			meminfo file of proc.
		"""
		def work():
			""" TODO: Add stop logic """
			while GechoGlobal.mem_monitor_active:
				time.sleep(GechoGlobal.mem_monitor_idle)
				for mem in gecho.procfs.meminfo():
					GechoGlobal.gechoQueue.put(mem)
					#print mem
		try:
			if GechoGlobal.mem_monitor_active == False:
				thread.start_new_thread(work,())
				GechoGlobal.mem_monitor_active = True
			else:
				GechoGlobal.mem_idle_time = idle
		except Exception as E:
			print "Unable to start CPU worker thread: %s", E

	@staticmethod
	def convertMegabytes(kb):
		""" Method used to return kilobytes to megabytes. """
		return kb / 1024

if __name__ == "__main__":
	ProcMem.spawn_memory_monitor(1);
	while True:
		pass
