"""
Will Dignazio
gecho 2013
"""

class ProcMemval(object):
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
	def convertMegabytes(kb):
		""" Method used to return kilobytes to megabytes. """
		return kb / 1024
