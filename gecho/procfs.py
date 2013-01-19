"""
Will Dignazio
gecho 2012
"""

class metaproc(type):
	def __new__(meta, classname, bases, classDict):
		print "Class Name: ", classname
		print "Bases: ", bases
		print "Class Attributes: ", classDict
		return type.__new__(meta, classname, bases, classDict)

class procfs(object):
	""" /proc Utility class """
	__metaclass__ = metaproc
