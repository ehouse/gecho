import daemon
import Queue
import time
import zmq
import jsonpickle

from daemon import runner
from gecho.procfs import *

# Global message queue construction
gechoQueue = Queue.Queue()

class gechod():
	""" gecho daemon """
	def __init__(self):
		self.stdin_path = '/dev/null'
		self.stdout_path = '/dev/tty'
		self.stderr_path = '/dev/tty'
		self.pidfile_path = '/tmp/gechod.pid'
		self.pidfile_timeout = 5

	def run(self):
		context = zmq.Context()
		socket = context.socket(zmq.PUB)
		socket.connect("tcp://127.0.0.1:5000") #TODO Configure in file
		while True:
			if not gechoQueue.empty():
				try:
					pubcontent = gechoQueue.get()
					if hasattr(pubcontent, "subscription"):
						jcontent = pubcontent.encode(pubcontent)
						print jcontent
					else:
						print "Popped non-publishable data, disposing."
				except:
					print "Exception popping queue content."

app = gechod()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
