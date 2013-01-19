import daemon
import Queue
import time
import zmq

from daemon import runner
from gecho.procfs import *

gechoQueue = Queue.Queue()
gechoQueue.put("test")

class gechod():
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
					print "Popping Message"
					pubcontent = gechoQueue.get()
				except:
					pass

app = gechod()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
