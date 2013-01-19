"""
Will Dignazio
gecho 2013
"""

import os
import glob

from gecho.cpu import ProcCPU
from gecho.memory import ProcMemval

class procfs(object):
	""" /proc Utility class """

	@staticmethod
	def get_cpus():
		""" Gets the cpus from /proc/stat """
		cpus = []
		stat = open('/proc/stat')
		for line in stat.readlines():
			attrs = line.split(' ')
			if "cpu" in attrs[0]:
				cpus.append(ProcCPU(attrs[0].strip(), #name
									attrs[1].strip(), #user
									attrs[2].strip(), #niced
									attrs[3].strip(), #system
									attrs[4].strip(), #idle
									attrs[5].strip(), #iowait
									attrs[6].strip(), #irq
									attrs[7].strip()))#softirq
		return cpus

	@staticmethod
	def meminfo():
		""" gets the memory info from /proc/meminfo """
		memblocks = []
		meminfo = open('/proc/meminfo')
		for line in meminfo.readlines():
			attrs = line.split(':')
			memblocks.append(ProcMemval(attrs[0].strip(), attrs[1].strip()))
		return memblocks
