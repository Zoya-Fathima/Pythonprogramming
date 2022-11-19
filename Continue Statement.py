#if condition is satisfied we skip the statement
#Printing n natural number divisible by 5
number=0
end_point=(int(input("Enter the end point")))
while number < end_point:
    number=number+1
    if number %5 == 0:
        print(number)
    else:
        continue
