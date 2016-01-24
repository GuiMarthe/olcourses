import re

file = open("regex_sum_210311.txt")

num = list()

## Finding the numbers

for line in file :      
    line = line.rstrip()
    y = re.findall('([0-9]+)', line)   # magic of regular expressions!
    num.append(y)


num = sum(num, []) ## Falttening the list

## looping for the total

total = 0 

for i in num :

    i = float(i)
    total = total + i
print total