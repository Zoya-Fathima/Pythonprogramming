print("Marks list")
n=int(input("Number of subjects"))
l=[]
for i in range(n):
    ele=int(input("Enter the Marks: "))
    l.append(ele)
print(l)
addition=sum(l)
print("adddition=:",addition)
average=addition/n
print("average=:",average)
if (average>=90):
    print("Distinction")
elif (average>=80)and(average<90):
    print("First class ")
elif(average>=70)and(average<60):
    print("Second class")
elif(average<=60)and(average>35):
    print("Pass")
else:
    print("Fail")