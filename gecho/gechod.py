import daemon
import Queue
import time
import zmq
import jsonpickle

from daemon import runner
from gecho.procfs import *
from gecho.cpu import ProcCPU
from gecho.memory import ProcMem
from gecho import GechoGlobal, GechoGlobal

# Global message queue construction
#gechoQueue = Queue.Queue(1000)

class gechod():
	""" gecho daemon """
	def __init__(self):
		self.stdin_path = '/dev/null'
		self.stdout_path = '/dev/tty'
		self.stderr_path = '/dev/tty'
		self.pidfile_path = '/tmp/gechod.pid'
		self.pidfile_timeout = 5

	def run(self):
		ProcCPU.spawn_cpu_monitor(1) #Spawn CPU monitor
		ProcMem.spawn_memory_monitor(1)
		context = zmq.Context()
		socket = context.socket(zmq.PUB)
		socket.bind("tcp://0.0.0.0:5000") #TODO Configure in file
		while True:
			time.sleep(GechoGlobal.verbosity) # Main idle wait, keeps CPU from hemorraging (spelling?)
			if not GechoGlobal.gechoQueue.empty():
				pubcontent = GechoGlobal.gechoQueue.get()
				if hasattr(pubcontent, "subscription"):
					jcontent = jsonpickle.encode(pubcontent)
					socket.send_multipart([pubcontent.subscription, jcontent])
					#print pubcontent.subscription, jcontent
				else:
					print "Popped non-publishable data, disposing."

app = gechod()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
