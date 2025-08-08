import math

again = 1

while again == 1:
    a = int(input("enter a : "))
    b = int(input("enter b : "))
    c = int(input("enter c : "))

    delta = b**2 - 4*a*c
    
    if delta == 0:
        delta = -b / 2*a
        print( "Single root: x = " , delta )
        
    elif delta >= 0:
        x1 = (-b + math.sqrt( delta )) / 2*a
        x2 = (-b - math.sqrt( delta )) / 2*a
        print ( "Two real roots: x1 = " , x1 ,"and x2 = ",x2 )

    else :
        print("No real roots")
        
    again = input("Wanna solve another equation? (yes/no) ")
    if again == "yes" :
        again = 1
        print("\n ")
    else :
        again == 0
        print(" Thanks for using the quadratic solver. See ya! ")

    


