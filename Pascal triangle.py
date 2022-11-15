#i is row and j is coloumn
print(("pascal traingle"))
n=int(input("Enter the last number in pascal triangle"))
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end='')
    print("")