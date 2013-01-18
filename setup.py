import multiprocessing, logging 
import sys

version="0.0.1"

readme_fp = fopen('README')
long_description = f.read.strip()
f.close()

install_requires = [ ]

setup(name="gecho",
        version=version,
        long_description=long_description,
        classifiers=[
            "Programming Language :: Python :: 2.7",
            "License :: OSI Approved :: GNU General Public License (GPL)",
            "Intended Audience :: Developers"
            ],
        keywords="gecho monitor distributed",
        author="Ethan House, Will Dignazio",
        licence="GPLv2",
        package=find_packages(exlcude=['ez_setup', 'examples', 'tests']), 
        author_email="slackwill@csh.rit.edu",
        include_package_data=True,
        zip_safe=False,
        install_requires=install_requires)
