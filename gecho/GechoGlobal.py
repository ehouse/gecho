import gecho
import Queue

"""
	The verbosity setting for the main thread, in other words
	the idle time between the popping of publishing data between
	cpu cycles. A value of 1 means 1 message per second, etc.
"""
verbosity = 0.1

"""
	I can't freaking believe I have to do this
	in order to share variables across modules
	sanely. I thought this was a joke, I was sadly
	mistaken.
"""
gechoQueue = Queue.Queue(1000) # Fill in with parsed config value

"""
	The gecho cpu monitor active and idle time fields, keeps
	track of the activity of the monitor, and its increment of
	activity.
"""
cpu_monitor_active = False
cpu_monitor_idle = 1

"""
	The gecho memory monitor active and idle time fields, just
	like the cpu monitor, keeps track of whether it is active and
	the idle time between increments.
"""
mem_monitor_active = False
mem_monitor_idle = 1

"""
	The gecho mdadm monitor active and idle time fields,
	monitors the /proc/mdstat file for changes in raid arrays.
	This feature requires proper access to the /proc/mdstat file,
	it typically has root privileges.
"""
mdadm_monitor_active = False
mdadm_monitor_idle = 1
