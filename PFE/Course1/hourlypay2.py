
hours = float(raw_input("please enter hours effectively worked: "))

rate = float(raw_input("please enter hourly rate: "))

if hours > 40 :
   p = 40*rate + (hours-40)*(rate*1.5)
else :
    p = rate*hours

print p



