## Write a program to read through the mbox-short.txt and figure out who has 
## the sent the greatest number of mail messages. The program looks for 
## 'From ' lines and takes the second word of those lines as the person 
## who sent the mail. The program creates a Python dictionary that maps the 
## sender's mail address to a count of the number of times they appear in the file. 
## After the dictionary is produced, the program reads through the dictionary 
## using a maximum loop to find the most prolific committer.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

file = open(name)

lemails = dict()

ll = list()

for line in file  :         ## Creating a list

    if line.strip().startswith("From ") : ll.append(line.split()[1])
    
for email in ll:            ## adding the elements from the list in the dictionary.
    if email in lemails :  lemails[email] = lemails[email] + 1
    else : lemails[email] = 1
    
## Following there are tow different methods for getting the maximum "key , value" in a dictionary. The first one seems more elegant.

## Method 1

high_value = max(lemails, key=lemails.get)
print high_value, lemails[high_value]

## Method 2 
   
max_value = 0
    
for key in lemails :
   
   if max_value < lemails[key] : 
      
      max_value = lemails[key]
      max_key = key

print max_key, max_value 