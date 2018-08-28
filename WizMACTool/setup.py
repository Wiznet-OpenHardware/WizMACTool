from distutils.core import setup
import py2exe, sys, os
from glob import glob

sys.argv.append('py2exe')

setup(
	options = {'py2exe':{
                'bundle_files':1,
               }
    },
	windows = [{
				'script':'WizMACTool.py',
				}],
	zipfile = None,
)

