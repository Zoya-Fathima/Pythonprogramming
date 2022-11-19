number=0
end_point=(int(input("Enter the end point")))
while number < end_point:
    number=number+1
    if number %5 == 0:
        continue
    else:
        print(number)


