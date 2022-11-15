cube=0
sum=0
average=0
print("please enter 10 numbers")
for i in range(1,11):
    num=int(input("Number%d= "%i))
    cube=num*num*num
    print("cube is ", cube)
    sum=sum+cube
    print("Sum is ",sum)
    average=sum/num
    print("Average is ",average)