#!python
import multiprocessing, logging
import sys
from setuptools import setup, find_packages

version="0.0.1"

readme_fp = open('README')
readme_fp.close()

install_requires = [ ]

setup(name="gecho",
		packages=["gecho"],
		requires=["PySensors", "pyzmq", "python-daemon", "jsonpickle", "pyinotify"],
		version=version,
		classifiers=[
			"Programming Language :: Python :: 2.7",
			"License :: OSI Approved :: GNU General Public License (GPL)",
			"Intended Audience :: Developers"
			],
		keywords="gecho monitor distributed",
		author="Ethan House, Will Dignazio",
		license="GPLv2",
		author_email="slackwill@csh.rit.edu",
		include_package_data=True,
		zip_safe=False,
		install_requires=install_requires)
