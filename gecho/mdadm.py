"""
Will Dignazio
gecho 2013
"""

import time
import thread
import gecho
from gecho.procfs import *
from gecho import GechoGlobal
import jsonpickle

class ProcMDADM(object):
	""" /proc/mdadm RAID Entry """
	def __init__(self, name,status, personality, members):
		self.name = name
		self.status = status
		self.members = members
		self.personality = personality

	def __str__(self):
		return self.name + " " + self.status + " " + explode(self.members)

	@staticmethod
	def spawn_mdadm_monitor(idle):
		""" Spawns a MDADM monitor, returns a reference to it. """
		def work():
			while GechoGlobal.mdadm_monitor_active:
				time.sleep(GechoGlobal.mdadm_monitor_idle)
				for raid in gecho.procfs.mdstat():
					GechoGlobal.gechoQueue.put(raid)
		try:
			if GechoGlobal.mdadm_monitor_active == False:
				thread.start_new_thread(work, ())
				GechoGlobal.mdadm_monitor_active = True
			else:
				GechoGlobal.mdadm_monitor_active = True
		except Exception as e:
			print "Unable to start MDADM worker thread: %s", e

if __name__ == "__main__":
	ProcMDADM.spawn_mdadm_monitor(1)
	while True:
		pass
