import time
import pysftp
# from watchdog.observers import Observer
# from watchdog.events import  PatternMatchingEventHandler
import datetime
import stat

dirToWatch = "/home/hinclude"
fileList = []
timeToSleep = 5
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
sftp=pysftp.Connection(host='192.168.1.31', username='hinclude',port=22,password='hinclude',cnopts=cnopts)
print(sftp)
print(sftp.pwd)
dirToWatch = sftp.pwd

print('sftp path')
g='/Users/apple/Desktop/venkatesh'
print(dirToWatch)# import the modules
s = sftp.isdir

while True:
	
	
	newFileList = sftp.listdir(dirToWatch)
    
	
	if fileList != newFileList:
		print(f"changes detected in {dirToWatch}:")
		changes = set(newFileList) - set(fileList)
		#files = glob.glob(dirToWatch)
		if changes>set():
			for fileattr in sftp.listdir_attr('/home/hinclude'):
				if stat.S_ISDIR(fileattr.st_mode):
					print('folder crae',fileattr,dirToWatch,datetime.datetime.now())
					
					break

				else:
					print('file created',fileattr,dirToWatch,datetime.datetime.now())
					print('file name',fileattr)
					#sftp.get(localpath='/home/hinclude/fileattr',remotepath='/Users/apple/Desktop/venkatesh',callback=None)
					break
					
		# 	for i in changes:
				
		# 		print(i)
		# 		if i in os.path.abspath('/home/hinclude'):
				
				
		# 			print('file  craeted',changes,dirToWatch,datetime.datetime.now())
		# 			break
		# 		else:
		# 			print('folder created',dirToWatch,changes,datetime.datetime.now())
		# 			sftp.get('/home/hinclude/changes','Users/apple/venkatesh')
		# 			break
		else:	
		
			print('file deleted',changes,dirToWatch,datetime.datetime.now())
			
		
		print(f"changes detected in {dirToWatch}:")
		#changes = set(newFileList) - set(fileList)
        
		#print('file delted',changes,dirToWatch,datetime.datetime.now())
        #print(glob.glob('/home/hinclude/*'))
		
		fileList = newFileList
	else:
		print("no new changes")
	time.sleep(timeToSleep)
