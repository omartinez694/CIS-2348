def file_op():
# you need a dictionary of the months i mean come on
    month_list = {'January': 1,'February': 2,'March': 3,'April': 4,'May': 5,'June': 6,'July': 7,'August': 8,'September': 9,'October': 10,'November': 11,'December': 12}
#open file
    with open('InputDates.txt') as file1:
      list1 = file1.read().splitlines()

      i = 0
      list2 = []
      while(list1[i] != "-1"):
        string1 = ""
        new_lis = list1[i].split(" ")
        #checking month and date ending with comma and year you know
        if(new_lis[0].lower() in month_list.keys() and new_lis[1].endswith(',') and (int(new_lis[2])>= 1000 and int(new_lis[2])<=2020)):
          string1 += str(month_list[new_lis[0].lower()]) + '/' + new_lis[1][:-1] + '/' + new_lis[2] + '\n'

          list2.append(string1)

      i += 1
#if the file is not their it will create a new one hopefully
    file2 = open('parsedDates.txt', 'w+')
#you need lines ofcourse
    file2.writelines(list2)
    file2.close()
file_op()
