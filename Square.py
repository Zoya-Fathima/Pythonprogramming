square=0
sum=0
average=0
print("please enter 10 numbers")
for i in range(1,11):
    num=int(input("Number%d= "%i))
    square=num*num
    print("square is ", square)
    sum=sum+square
    print("Sum is ",sum)
    average=sum/num
    print("Average is ",average)
