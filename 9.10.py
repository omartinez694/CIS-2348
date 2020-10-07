import csv
file = input()
freqlist = {}
with open(file, 'r') as cvsfile:
    words_reader = csv.reader(cvsfile)
    row = next(words_reader)
    for word in row:
        if word in freqlist:
            freqlist[word] += 1
        else:
            freqlist[word]=1
for w in freqlist:
    print (w, freqlist[w])