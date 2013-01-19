"""
Will Dignazio
gecho 2013
"""

import os
import glob

from gecho.cpu import ProcCPU

class procfs(object):
	""" /proc Utility class """
	@staticmethod
	def get_cpus():
		cpus = []
		stat = open('/proc/stat')
		for line in stat.readlines():
			attrs = line.split(' ')
			if "cpu" in attrs[0]:
				cpus.append(ProcCPU(attrs[0], #name
									attrs[1], #user
									attrs[2], #niced
									attrs[3], #system
									attrs[4], #idle
									attrs[5], #iowait
									attrs[6], #irq
									attrs[7]))#softirq
		return cpus

	@staticmethod
	def meminfo():
		memblocks = []
		meminfo = open('/proc/meminfo')
		for line in meminfo.readlines():
			attrs = line.split(':')
			memblocks.append(ProcMemval(attrs[0], attrs[1]))
		return memblocks

