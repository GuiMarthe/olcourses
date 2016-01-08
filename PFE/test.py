# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
if len(fname)== 0 :
    fname ="mbox-short.txt"

fh = open(fname)

## counting the total of lines

count = 0

for line in fh :

    count = count + 1 
    
print " total # of lines is: ", count


fh = open(fname)

countx = 0

for line in fh:
    if not  line.startswith("X-DSPAM-Confidence:") : continue
    countx = countx + 1
    pos = line.startswith("X-DSPAM-Confidence:").find(":")
   
  
    
print " total # of lines with 'X-DSPAM-Confidence:' is: ", countx

