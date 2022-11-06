# designing a simple chatbot using if else
print("Hello, I am a chatbot")
print("How may i help you?\n")
print("Hit 1 for software installation request")
print("Hit 2 for software update request")
print("Hit 3 for software uninstall request ")
print("Hit 4 for software repair request")
#accepting the users input
userInput = int(input("Enter your choice: "))
if userInput == 1:
    softwareNeeded = input("Please provide the software name")
elif userInput == 2:
    softwareUpdate = input("Please provide software name to be updated")
elif userInput == 3:
    softwareUninstall = input("Please provide the software name to be uninstalled")
elif userInput == 4:
    softwareRepair = input("Please provide the software name to be repaired")
else:
    otherRequest = input("Please provide the details of your request")
print("Thank you for using our service , Our team will get back to you soon")
