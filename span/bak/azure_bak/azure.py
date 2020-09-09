# -*- coding: utf-8 -*-
from azure.storage.blob import BlockBlobService
import os
from utc import get_utc_day

mystoragename = "virtualmachinesdiag817"
mystoragekey = "yFhi0df80NarvV3cPbHraHJLGsjUf29moFcSTq2glQQALWk5lv6wn+Z7bOsgEtD7IT4dj0wLGWxyuPihlQ868g=="
blob_service = BlockBlobService(account_name=mystoragename, account_key=mystoragekey)
print(blob_service)
# 下载一个 Blob Container 中的所有文件
def downloadFilesInContainer(blobContainName):
	generator = blob_service.list_blobs(blobContainName)
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

# 获得用户所有的 Blob Container
containerGenerator = blob_service.list_containers()
marker = None
#generator = blob_service.list_blobs("base-station", "2020/100", num_results=100, marker=marker)
print("test")
print (containerGenerator)

for con in containerGenerator:
	print(con.name)
	downloadFilesInContainer(con.name)















