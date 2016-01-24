import re

x = "Why should you 422 learn to write programs? 7746\n 12 1929 8827\n 7 an rewarding activity 8712"

num = re.findall('[0-9]+', x)

print num
