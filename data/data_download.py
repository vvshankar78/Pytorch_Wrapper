import os
import urllib.request
import zipfile
from random import shuffle
from math import floor


def download_dataset(args):
	print('Beginning dataset download with urllib2')
	url = args.url
	temp = '%s'+args.target_zip
	path = temp % os.getcwd()
	urllib.request.urlretrieve(url, path)
	print("Dataset downloaded")