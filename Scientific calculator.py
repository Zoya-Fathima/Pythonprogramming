import math
print("CASIO")
print("""
1-Addition
2-Subtraction
3-Multiplication 
4-Division
5-Power
6-Sine
7-Cosine
8-Tangent
9-Logorithm
10-Exponential
11-Squarroot
""")
option=input("enter your option")
if option=="1" or option=="2" or option=="3" or option=="4" or option=="5":
    a=float(input("Enter value of a :"))
    b=float(input("Enter value of b:"))

    if option=="1":
        print(a , "+" , b , "=" ,(a+b))
    elif option=="2":
        print(a , "-" , b , "=" ,(a-b))
    elif option=="3":
        print(a , "*" , b , "=" ,(a*b))
    elif option=="4":
        if b==0.0:
            print("Divide by 0 Error")
        else:
            print(a, "/" , b ,"=" ,(a/b))
    else:
        result=math.pow(a,b)
        print(a, "to the power", b , " times is: ", result)
else:
    a=float(input("Enter value of a :"))
    if option=="6":
        print("1.In radians \n2.In degrees")
        sin=input("Enter the type")
        if sin=="1":
            result=math.sin(a)
            print("The sin value of", a, "in radians is: ", result)
        else:
            rad=math.radians(a)
            result=math.sin(rad)
            pi=math.pi
            print("The sin value of", rad*180/pi , "in degrees is: ", result)
    elif option=="7":
        print("1.In radians \n2.In degrees")
        cos=input("Enter your choice")
        if cos=="1":
            result=math.cos(a)
            print("The cos value of", a, "in radians is: ", result)
        else:
            rad=math.radians(a)
            result=math.cos(rad)
            pi=math.pi
            print("The cos value of", rad*180/pi , "in degrees is: ", result)
    elif option=="8":
        print("1.In radians \n2.In degrees")
        tan=input("Enter your choice")
        if tan=="1":
            result=math.tan(a)
            print("The tan value of", a, "in radians is: ", result)
        else:
            rad=math.radians(a)
            result=math.tan(rad)
            pi=math.pi
            print("The tan value of", rad*180/pi , "in degrees is: ", result)
    elif option=="9":
        print("1.log base 10 \n2.log base e")
        log=input("Enter your choice")
        if log=="1":
            result=math.log10(a)
            print("The log value of", a, "is: ", result)
        else:
            result=math.log(a,2.718281828459045)
            print("The log base e value of", a, "is: ", result)
    elif option=="10":
        result=math.exp(a)
        print("exponential of" , a ,"is" , result)
    else:
        result=math.sqrt(a)
        print("squareroot of " , a ,"is" , result)
