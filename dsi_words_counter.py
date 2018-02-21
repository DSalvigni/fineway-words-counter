#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::Written by Daniele Salvigni::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#Developed by using python 3.x...................................



#path to the production file we want to counts...
data='data.txt'
#path to the test file we want to counts...- Uncomment to test the next line
test_data='test_data.txt'



#I open the file in r mode 
def counter_words(file):
	words = {}
	with open(file,'r', encoding='utf-8') as f:
		for readword in f.read().split():
			if readword not in words:
				words[readword] = 1
			else:
				words[readword] = words[readword] + 1
	f.close();
	#I print out the result
	for key,value in words.items():
		print("Word:"+str(key)+" -> occurs: "+str(value))


#test - Uncomment to test the next 2 lines
#print("this is my test:")print("this is my test:")
#counter_words(test_data)

#Productions
counter_words(data)

		
#To run it in production
#1 - Test with a pre-compiled file (we check what we expect)
#2 - Test with the given data file

#Alternative approach:
#1 - Using the reading byte mode (rb) byte if i do not provide the text encoding
#2 - Using Counter from collections
#3 - in case of big txt file we can evaluate the use of the the multiprocessing lib, in order to create "chunks" of the file
