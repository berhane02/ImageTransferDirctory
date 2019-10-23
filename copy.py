#Yemane Berhane lab01
import os.path
import hashlib
import sys
#ask for input file 
fileName = sys.argv[1]
outputFile = sys.argv[2]


def create_Directory(outputFile):
	if not os.path.exists(outputFile):
		os.makedirs(outputFile)
def compare(file):
	hasher = hashlib.md5()
	with open(file, 'rb') as open_file:
		content = open_file.read()
		hasher.update(content)
	print(hasher.hexdigest())
		
def transfer_File(fileName, outputFile):
	#check if file exit
	if(os.path.isfile(fileName)):
		bufferSize = 1000;
		#open file if exist
		with open(fileName, 'rb') as file:
			#outputFile = input("Enter output directory: ")
			create_Directory(outputFile)
			outfile = open(outputFile+"/"+fileName, "wb")
			#store date in a buffer to be written
			buffer = file.read(bufferSize);
			while len(buffer):
				outfile.write(buffer)
				buffer = file.read(bufferSize)
				file.flush()
			#close output file
			outfile.close()
			print('Done!')
			#compare file
			compare(fileName)
			compare("recv/"+fileName)
	#exit if file doesn't exists 
	else:
		print('file doesn exit goodby!')
transfer_File(fileName,outputFile)




