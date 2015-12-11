#this program will give you a letter grade based on you decimal (0 - 1) grade

try :

    grade = float(raw_input("Please enter you grade: "))

except :

    print "Error! Please enter a number between 0 and 1"
 
    quit()

if grade > 1 or grade < 0 :
    
    print "Please enter a number between 0 and 1"
        
    quit()
    
elif grade >= 0.9 :

    print "A"

elif grade >= 0.8 : 
    
    print "B"

elif grade >= 0.7 :
    print "C"
    
elif grade >= 0.6 :

    print "D"
    
elif grade < 0.6 :

    print "F"