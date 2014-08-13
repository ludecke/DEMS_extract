import os
import operator
import codecs

result = {}

for filename in os.listdir(os.getcwd()+"/data"):
	with open("data/"+filename, encoding='utf8') as f:
		keyword_found = False
		counter=0
		repetitions = 0
		for line in f:
			if line.startswith("--"):
				counter=0
				keyword_found = True
			if keyword_found and counter == 1:
				repetitions = int(line[26:30])
			if keyword_found and counter == 2:
				sapline = line.strip()
				if sapline not in result:
					result[sapline]=0
				result[sapline]+=repetitions


			counter+=1

print(result) 
sorted_result = sorted(result.iteritems(), key=lambda sapline: sapline[1], reverse=True)
print(sorted_result)

with open ("data/output_file.csv", 'w', encoding='utf8') as f:
	for sapline, count in sorted_result:
		f.write ("{};{}\n".format(sapline, count))

#python 3 auf mac installieren, aufruf mit "python3"
#utf-8 ausgeben




#for string, repetitions in result:

#hausaufgabe: sort dictionary by value
			
#if line.startswith("--"):