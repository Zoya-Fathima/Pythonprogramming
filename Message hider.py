msg=input("Enter the message")
ascii_msg=[]
char_msg=[]
for i in msg:
    ascii=ord(i)
    ascii=ascii+1
    ascii_msg.append(ascii)
for i in ascii_msg:
    code=chr(i)
    char_msg.append(code)
for i in char_msg:
    print(i,end='')