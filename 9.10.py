import csv

with open('input1.csv', mode='r') as wordsfile:
    words_reader = csv.reader(wordsfile)
for row in words_reader:
    list_of_words = set(row)
    for word in list_of_words:
        count = row.count(word)
        print(word, count)