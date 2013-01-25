"""
Will Dignazio
gecho 2013
"""

import os
import glob

import jsonpickle

from gecho.cpu import ProcCPU
from gecho.memory import ProcMem
from gecho.mdadm import ProcMDADM

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

def mdstat():
	""" Gets the RAID info from /proc/mdstat """
	raid = []
	stat = open("/proc/mdstat")
	for line in stat.readlines():
		if line[:2] == "md": # Entry starts with md[whatever]
			splitline = line.split(':')
			name = splitline[0].strip()
			print name
			info = splitline[1].split(' ' ) # Second half of raid entry
			print info
			status = info[0].strip()
			personality = info[1].strip()
			members = info[2:]
			for member in members:
				member.strip()
			entry = ProcMDADM(name, status, personality, members)
			raid.append(entry)
			print jsonpickle.encode(entry)
	return raid

def meminfo():
	""" gets the memory info from /proc/meminfo """
	memblocks = []
	meminfo = open('/proc/meminfo')
	for line in meminfo.readlines():
		attrs = line.split(':')
		memblocks.append(ProcMem(attrs[0].strip(), attrs[1].split()[0]))
	return memblocks
