import gecho
import Queue

"""
I can't freaking believe I have to do this
in order to share variables across modules
sanely. I thought this was a joke, I was sadly
mistaken.
"""
gechoQueue = Queue.Queue(100) # Fill in with parsed config value

"""
	The gecho cpu monitor active and idle time fields, keeps
	track of the activity of the monitor, and its increment of
	activity.
"""
cpu_monitor_active = False
cpu_monitor_idle = 1
