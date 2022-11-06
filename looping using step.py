start_point = int(input("Enter the satrt point : "))
endpoint = int(input("Enter the endpoint: "))
sum_of_numbers=0
for i in range(start_point,endpoint+1,-2 ):
    print(i)
    sum_of_numbers = sum_of_numbers + i
print(sum_of_numbers)



