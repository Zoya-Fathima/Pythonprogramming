msg=input("Enter the message")
ascii_values=[]
char_values=[]
for i in msg:
    ascii=ord(i)
    ascii=ascii+1
    ascii_values.append(ascii)
for i in ascii_values:
    code=chr(i)
    char_values.append(code)
for i in char_values:
    print(i,end='')


