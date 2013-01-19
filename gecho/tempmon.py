import sensors

class sensors(object):
	""" Util class for gathering sensor data """
	@staticmethod
	def print_features():
		for chip in sensors.iter_detected_chips():
			print "%s at %s" % (chip, chip.adapter_name)
			for feature in chip:
				print "%s: %.2f" % (feature.label, feature.get_value())

if __name__ == "__main__":
	sensors.print_features()
