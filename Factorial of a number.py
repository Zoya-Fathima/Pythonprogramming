print("Factorial of a Number")
num=int(input("Enter a Number: "))
factorial=1
if num in range(-1,0):
    print("factorial doesn't exist for negative numbers ")
elif num==0:
    print("The factorial of zero is 1 ")
else:
    print("The factorial of",num, "is")
    for i in range(1,num+1):
        factorial=factorial*i
        print( factorial )