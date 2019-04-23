import csv

def FrequencyBuilder(fileName):
	tempDictonary={}
	with open(fileName) as tsvfile:
		for line in tsvfile:
			(key,value) = line.split("\t")
			value=value.rstrip()
			tempDictonary[key]=value
	return tempDictonary

def PrintFunction(lst):
	for data in lst:
		print(data[1],"\t","(",data[0],")")


basePath=""
fileName=basePath+"word_frequency.txt"
contents=[]
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

lst=FrequencyBuilder(fileName)
l=[]

for data in contents:
	for word,frequency in lst.items():
		if(word.find(data)==0):
			l.append((int(frequency),word))
	l.sort(reverse=True)
	PrintFunction(l)
	print("\n")
	l=[]
