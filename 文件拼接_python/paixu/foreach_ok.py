import os

def EnumPathFiles(path, callback):
    if not os.path.isdir(path):
        print('Error:"',path,'" is not a directory or does not exist.')
        return
    list_dirs = os.walk(path)

    for root, dirs, files in list_dirs:
        for d in dirs:
            EnumPathFiles(os.path.join(root, d), callback)
        for f in files:
            callback(root, f)

def callback1(path, filename):
    print(path+'\\'+filename)



for dir_name, dirs, file_names in os.walk("../"):

    

    # 1. Full directory.

    print (dir_name)

    

    # 2. Full path.

    for file_name in file_names:

        print (os.path.join(dir_name, file_name))


#EnumPathFiles("../", callback1)

