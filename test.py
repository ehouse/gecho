from gecho.procfs import *
import zmq
from zmq import devices
import time

if __name__ == "__main__":
	cpus = procfs.get_cpus()
	for cpu in cpus:
		print cpu
	memory = procfs.meminfo()
	for mem in memory:
		print mem

	context = zmq.Context()
	socket = context.socket(zmq.REP)
	socket.bind("tcp://127.0.0.1:5000")
	print "starting blocking loop"
	while True:
		msg = socket.recv()
		print "got", msg
		socket.send(msg)
