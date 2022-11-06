Marks1 = int(input("Enter Marks of first test"))
Marks2 = int(input("Enter marks of second test"))
Marks3 = int(input("Enter marks of third test"))
if(Marks1<Marks2 and Marks1<Marks3):
    print((Marks2+Marks3)/2)
elif(Marks2<Marks1 and Marks2<Marks3):
    print((Marks1+Marks3)/2)
else:
    print((Marks1+Marks2)/2)
