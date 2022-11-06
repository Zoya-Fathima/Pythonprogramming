endPoint = int(input("Enter the value of endPoint: "))
sum_of_numbers = 0
i=0
while i<= endPoint:
    sum_of_numbers = sum_of_numbers+i
    i=i+1
print("The sum of first {} whole numbers is {} ".format(endPoint,sum_of_numbers))