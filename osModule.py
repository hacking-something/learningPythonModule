import os

getcwd = os.getcwd()
print('0:%s' % getcwd)

fileName = __file__
print('1:%s' % fileName) # 'osModuble.py'

filePathName = os.path.realpath(fileName)
print('2:%s' % filePathName) # 'C:\Users\Faynman\Desktop\learningPythonModule\osModuble.py'

print(os.path.split(filePathName))

if os.path.isdir(filePathName):
	print('3: This is a directory.')
else:
	print("3: This isn't a directory.")

if os.path.isfile(filePathName):
	print('4: This is a file.')
else:
	print("4: This isn't a file.")	
	
filePath = os.path.dirname(filePathName)
print('5:%s' % filePath) # 'C:\Users\Faynman\Desktop\learningPythonModule'

newFilePath = os.path.join(filePath, 'octoprint')
print('6:%s' % newFilePath) # 'C:\Users\Faynman\Desktop\learningPythonModule\octoprint'

newFilePath1 = os.path.join('src', 'octoprint', "translations")
print('6:%s' % newFilePath1) # 'src\octoprint\translations'

if os.path.exists(newFilePath):
	#os.chdir(newFilePath)
	print('7: Project directory in: %s' % newFilePath)
else:
	print("7: Project directory isn't exists!!!")

print(os.getcwd())