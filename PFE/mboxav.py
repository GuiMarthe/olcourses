fname = raw_input("Enter file name: ")
fh = open(fname)

x = 0
total = 0
for line in fh:
    if not line.strip().startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(":")
    number = float(line[pos+1:].lstrip())
    x = x+1
    total = total + number

avg = total/x
print "Average spam confidence:", avg