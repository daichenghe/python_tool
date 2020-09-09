import os
import time
def file_search(root_dir,signle_search):
    print ('start')
    for root,dirs,files in os.walk(root_dir):
        #print root
        #print dirs
        if signle_search == True:
            return dirs
        #print files
route = file_search('/media/pi/',True)
print route
print 'route1 = %s' % route[0]
path = os.path.join('/media/pi',route[0],'123.txt')
print path
fh = open(path,'wa')
fh.close
