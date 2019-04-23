import csv

def MapBuilder(fileNameIn1):
	tempDictonary={}
	with open(fileNameIn1) as tsvfile:
		for line in tsvfile:
			(value, key) = line.split("\t")
			key=key.rstrip()
			tempDictonary[key]=value
	return tempDictonary

def ReplacementFunction(fileNameIn2,l):
	tempDictonary={}
	with open(fileNameIn2) as tsvfile:
		for line in tsvfile:
			(value,key) = line.split("\t")
			key=key.rstrip()
			for st,st1 in l.items():
				if(st in key):
					key=key.replace(st,st1)
			tempDictonary[key]=value
	return tempDictonary


basePath=""
fileNameIn1=basePath+"character_mapping.txt"
fileNameIn2=basePath+"word_corpus.txt"
fileNameOut=basePath+"word_frequency.txt"


lst=MapBuilder(fileNameIn1)

try:
    del lst["Represented by"]
except KeyError:
    print("Key 'Represented by' not found")

lst=list(lst.items())
lst.sort(reverse=True)
lst=dict(lst)

lst1=ReplacementFunction(fileNameIn2,lst)

try:
    del lst1["Word"]
except KeyError:
    print("Key 'Word' not found")

with open(fileNameOut, 'wt') as out_file:
    for key in lst1.keys():
	    out_file.write("%s\t%s\n"%(key,lst1[key]))

