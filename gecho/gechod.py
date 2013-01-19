import daemon
import Queue
import time
import zmq
import jsonpickle

from daemon import runner
from gecho.procfs import *

# Global message queue construction
gechoQueue = Queue.Queue()

for cpu in procfs.get_cpus():
	gechoQueue.put(cpu)

class gechod():
	""" gecho daemon """
	def __init__(self):
		self.stdin_path = '/dev/null'
		self.stdout_path = '/dev/tty'
		self.stderr_path = '/dev/tty'
		self.pidfile_path = '/tmp/gechod.pid'
		self.pidfile_timeout = 5

	def run(self):
		ProcCPU.spawn_cpu_monitor(1)
		context = zmq.Context()
		socket = context.socket(zmq.PUB)
		socket.connect("tcp://127.0.0.1:5000") #TODO Configure in file
		while True:
			time.sleep(1)
			for cpu in procfs.get_cpus():
				gechoQueue.put(cpu)
			if not gechoQueue.empty():
				pubcontent = gechoQueue.get()
				if hasattr(pubcontent, "subscription"):
					jcontent = jsonpickle.encode(pubcontent)
					socket.send_multipart([pubcontent.subscription, jcontent])
					print pubcontent.subscription, jcontent
				else:
					print "Popped non-publishable data, disposing."

app = gechod()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
