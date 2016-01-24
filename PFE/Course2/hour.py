## Write a program to read through the mbox-short.txt and figure out the 
## distribution by hour of the day for each of the messages. 
## You can pull the hour out from the 'From ' line by finding 
## the time and then splitting the string a second time using a colon.
## From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

## Once you have accumulated the counts for each hour, 
## print out the counts, sorted by hour as shown below.

## suggested start

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
file = open(name)
ll = list()
hrll = list()
tblhrs = dict()


for line in file  :         ## Creating a list of email's sent times 

    if line.strip().startswith("From ") : ll.append(line.split()[5])

for hr in ll :  
   if hr.split(':')[0] in tblhrs : tblhrs[hr.split(':')[0]] = tblhrs[hr.split(':')[0]] + 1
   else : tblhrs[hr.split(':')[0]] = 1

##for i in tblhrs : print i , tblhrs[i]

t = sorted(tblhrs.items())
for k, v in t  : print k, v