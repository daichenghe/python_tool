from abc import ABCMeta, abstractmethod
import os
import sys
import threading
import operator
import datetime
import collections
import time
import struct
import traceback
from pathlib import Path
#from ...framework.utils import helper
#from ...framework.file_storage import FileLoger
from azure.storage.blob import BlockBlobService
if sys.version_info[0] > 2:
    from queue import Queue
else:
    from Queue import Queue
import requests
import json


def on_upgarde_failed(warning):
	print(warning)

def thread_do_upgrade_framework(file):
	try:
		# step.1 download firmware
		if not download_firmware(file):
			on_upgarde_failed('cannot find firmware file')
			return
	except Exception as e:
		on_upgarde_failed('Upgrade Failed')
		traceback.print_exc()
'''
def write_firmware(self):
	while self.addr < self.fs_len:
		packet_data_len = self.max_data_len if (
			self.fs_len - self.addr) > self.max_data_len else (self.fs_len - self.addr)
		data = self.fw[self.addr: (self.addr + packet_data_len)]
		self.write_block(packet_data_len, self.addr, data)
		self.addr += packet_data_len
		self.add_output_packet('stream', 'upgrade_progress', {
			'addr': self.addr,
			'fs_len': self.fs_len
		})
'''

def download_firmware(file):

	#print(res.text)
	if not os.path.exists('upgrade'):
		os.makedirs('upgrade')

	firmware_file_path = os.path.join('upgrade', file)
	firmware_file = Path(firmware_file_path)

	if firmware_file.is_file():
		fw = open(firmware_file_path, 'rb').read()
	else:
		block_blob_service = BlockBlobService(
			account_name='navview', protocol='https')
		block_blob_service.get_blob_to_path(
			'apps', file, firmware_file_path)
		fw = open(firmware_file_path, 'rb').read()

	print('upgrade fw: %s' % file)
	max_data_len = 240
	addr = 0
	fs_len = len(fw)
	return True

def get_file_list():
	try:
		upgarde_root = os.path.join(os.getcwd(), 'upgrade')
		url = "https://api.aceinna.com/api/userApps/queryAll"
		data = {"type": 0,"categories": [4]}
		res = requests.post(url=url,data=data)
		#json_str = json.dumps(res)
		json_str = json.loads(res.text)
		#print (json_str)
		name = []
		for json_item in json_str:
			print (json_item['name'])
			print (json_item['id'])
			file_item = []
			file_item.append(json_item['name'])
			file_item.append(json_item['id'])
			name.append(file_item)
		return name
	except:
		print("can not connect to network")

def get_file_name(id):
	try:
		data = {"id": id}
		url = "https://api.aceinna.com/api/userApps/details"
		res = requests.post(url=url,data=data)
		json_str = json.loads(res.text)
		#print(json_str)
		bin_versions = json_str.get('versions')
		#print(bin_versions)
		bin_name = bin_versions[0]['fileName']
		print(bin_name)
		return bin_name
	except:
		print("can not connect to network")


'''
ret = get_file_list()
data = {"id": 317}
url = "https://api.aceinna.com/api/userApps/details"
res = requests.post(url=url,data=data)
print(res.text)
'''



	
	