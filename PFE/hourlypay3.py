
def computepay(h,r) :
    
    if h > 40 :
        p = 40*r + (h-40)*(r*1.5)
    else :
        p = r*h
    return p
    
    

hours = float(raw_input("please enter hours effectively worked: "))

rate = float(raw_input("please enter hourly rate: "))

pay = computepay(hours,rate)

print pay
