start_point=int(input("Enter the start point:"))
end_point=int(input("Enter the end point"))
print("The even numbers between" , start_point ,"and" , end_point , "is:")
for i in range(start_point,end_point+1):
    if i%2==0:
        print(i ,end=" ")