start_point=int(input("Enter the start point:"))
end_point=int(input("Enter the end point:"))
n=1
sum=0
while n<=end_point:
    sum=sum+n*n*n
    avg=sum/((end_point+1)-start_point)
    print("cube of ", n , "is" , n*n*n)
    n=n+1
    print("sum is",sum)
    print("avg is",avg)