import os
import shutil
def split_file():
	splitLen = 1000
	outputBase = 'SplittedData/data'
	input = open('InputedData/data.txt', 'r').read().split('\n')
	i=1
	for lines in range(0, len(input), splitLen):
		outputData= input[lines:lines+splitLen]
		output = open(outputBase+str(i)+'.txt','w')
		output.write('\n'.join(outputData))
		output.close()
		i+=1
	print("File is splitted successfully!")

def merge_file():
	with open('MergedData/data.txt', 'wb') as fdst:
		sourcepath = 'SplittedData/'
		for subdir, dirs, files in os.walk(sourcepath):
			for file in files:
				filename= sourcepath+file
				with open(filename, 'rb') as fsrc:
					shutil.copyfileobj(fsrc,fdst,1024*1025*10)
	print("File is merged successfully!")




if __name__=="__main__":
	split_file()
	merge_file()
