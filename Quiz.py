print("Take our quiz to test your knowledge on C Programming")
print("Each correct answer will be rewarded with a point and no negative marking")
print("LETS BEGIN")
Ans=input("1.Which is valid C expression? \n options:a) int my_num = 100,000; \n b) int my_num = 100000; \n c) int my num = 1000; \n d) int $my_num = 10000;")
if Ans=='b':
    print("Correct")
    print(" +1 point")
else:
    print("incorrect")
    print("The answer is option b \n explaination:Space, comma and $ cannot be used in a variable name")
Ans=input("2.Which of the following declaration is not supported by C language? \n a) String str;\n b) char *str;\n c) float str = 3e2;\n d) Both String str; & float str = 3e2;")
if Ans=='a':
    print("Correct")
    print("+1 point")
else:
    print("incorrect \n Explanation: It is legal in Java, but not in C language")
Ans=input("3.Property which allows to produce different executable for different platforms in C is called? \n a) File inclusion \n b) Selective inclusion \n c) Conditional compilation \n d) Recursive macros \n")
if Ans=='c':
    print("Correct")
    print("+1 point")
else:
    print("incorrect \n Explanation: Conditional compilation is the preprocessor facility to produce a different executable.")
Ans=input("4. The C-preprocessors are specified with ___ symbol. \n a) # \n b) $ \n c) ” ” \n d) &  ")
if Ans=='a':
    print("Correct")
    print("+1 point")
else:
    print("incorrect \n Explanation: The C-preprocessors are specified with # symbol.")
Ans=input("5.Which of the following is not an operator in C? \n a) , \n b) sizeof() \n c) ~ \nd) None of the mentioned")
if Ans=='d':
    print("Correct")
    print("+1 point")
else:
    print("incorrect \n none")