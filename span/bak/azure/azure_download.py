# -*- coding: utf-8 -*-
from azure.storage.blob import BlockBlobService
import os
from utc import get_utc_day,file_search


# 下载一个 Blob Container 中的所有文件
'''
def downloadFilesInContainer(blobContainName):
	generator = blob_service.list_blobs(blobContainName)
	print("generator.name = %s" % generator)
	for blob in generator:
	   # 获得 Blob 文件的目录路径
	   blobDirName =  os.path.dirname(blob.name)
	   print("blobDirName = %s" % blobDirName)
	   print("blob.name = %s" % blob.name)
	   # 把 Blob Container 的名称也添加为一级目录
	   newBlobDirName = os.path.join(blobContainName, blobDirName)
	   print("newBlobDirName = %s" % newBlobDirName)
	   # 检查文件目录是否存在，不存在就创建
	   if not os.path.exists(newBlobDirName):
		   os.makedirs(newBlobDirName)
	   localFileName = os.path.join(blobContainName, blob.name)
	   print("localFileName = %s" % localFileName)
	   blob_service.get_blob_to_path(blobContainName, blob.name, localFileName)
'''

def downloadFilesInContainer(blob_service,blobContainName,utc_year,utc_day,utc_hour):
	dir = utc_year + '/' + utc_day
	print(dir)
	generator = blob_service.list_blobs(blobContainName,dir)
	print("utc_hour = %d" % int(utc_hour))
	base_min = chr(int(utc_hour[1:2]) + 97)
	base_max = chr(int(utc_hour[1:2]) + 104)
	print("base_min = %s" % base_min)
	for blob in generator:
		# 获得 Blob 文件的目录路径
		#print("test = %s" % blob.name[-6])
		if ('wx02' in blob.name) and (blob.name[-6] >= base_min) and (blob.name[-6] < base_max):
			blobDirName =  os.path.dirname(blob.name)
			print("blob.name = %s" % blob.name)
			# 把 Blob Container 的名称也添加为一级目录
			newBlobDirName = os.path.join(blobContainName, blobDirName)
			# 检查文件目录是否存在，不存在就创建
			if not os.path.exists(newBlobDirName):
				os.makedirs(newBlobDirName)
			localFileName = os.path.join(blobContainName, blob.name)
			print("localFileName = %s" % localFileName)
			blob_service.get_blob_to_path(blobContainName, blob.name, localFileName)
		else:
			continue

# 获得用户所有的 Blob Container
mystoragename = "virtualmachinesdiag817"
mystoragekey = "yFhi0df80NarvV3cPbHraHJLGsjUf29moFcSTq2glQQALWk5lv6wn+Z7bOsgEtD7IT4dj0wLGWxyuPihlQ868g=="
blob_service = BlockBlobService(account_name=mystoragename, account_key=mystoragekey)

containerGenerator = blob_service.list_containers()
marker = None
#generator = blob_service.list_blobs("base-station", "2020/100", num_results=100, marker=marker)
'''
blobs = blob_service.list_blobs()
for blob in blobs:
	print(blob.name)
'''
#downloadFilesInContainer('base-station')

for con in containerGenerator:
	time_list = []
	if 'base-station' in con.name:
		print(con.name)
		print('test')
		dir,files = file_search('./',1)
		print(dir)
		print(files)
		for file in files:
			if ('novatel' in file) and ('.bin' in file):
				print("select file is: %s" % file)
				file_time = file[-23:-4]
				time_list = file_time.split('_')
				print(time_list)
		utc_day,utc_year,utc_hour = get_utc_day(time_list)
		downloadFilesInContainer(blob_service,con.name,utc_year,utc_day,utc_hour)
		'''
		generator = blob_service.list_blobs(con.name,'2020')
		for blob in generator:
			print("blob.name = %s" % blob.name)
		'''














