import os

def file_convbin_file(root_dir):
	for root,dirs,files in os.walk(root_dir):
		for filename in files:
			if ('convbin.exe' in filename):
				return os.path.join(root, filename)
				
file_path = file_convbin_file('./')

print(file_path)