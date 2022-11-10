print("Welcome to troubleshoot")
print("choose the problem you are facing present below")
print("option1=Speaker")
print("option2=Internet")
print("option3=Printer")
print("option4=Windows operation")
option=int(input("Enter the problem"))
if option==1:
    print("Go to sound setting and set audio devices as a default devices")
elif option==2:
    print("Go to wifi and connect by entering password")
elif option==3:
    print=("Connect to cloud print and install the drive")
elif option==4:
    option=input("go to task manager and click properties if updation problem say yes/no")
    if option=="yes":
        print("Go to settings and click on updation")
    else:
        print("Restart the windows")
else:
    print("We can't understand")


