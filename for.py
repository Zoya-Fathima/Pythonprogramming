number=0
end_point=(int(input("Enter the end point")))
for i in range(end_point):
    number=number+1
    if number%5==0:
        print(number)
    else:
        continue
