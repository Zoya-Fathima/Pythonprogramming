print("Take our quiz to test your knowledge on C Programming")
print("Each correct answer will be rewarded with a point and no negative marking")
print("LETS BEGIN")
score = 0
Ans = input(
    "1.Which is valid C expression? \n options:a) int my_num = 100,000 \n b) int my_num = 100000 \n c) int my num = 1000 \n d) int $my_num = 10000 \n")
if Ans == 'b':
    print("\n Correct")
    print(" +1 point \n")
    score = score + 1
else:
    print(
        "\n incorrect \nThe answer is option b \n explaination:Space, comma and $ cannot be used in a variable name\n")
Ans = input(
    "2.Which of the following declaration is not supported by C language? \n a) String str\n b) char *str\n c) float str = 3e2\n d) Both String str & float str = 3e2 \n")
if Ans == 'a':
    print("\n Correct")
    print("+1 point \n")
    score = score + 1

else:
    print("\n incorrect \n Explanation: It is legal in Java, but not in C language \n")
Ans = input(
    "3.Property which allows to produce different executable for different platforms in C is called? \n a) File inclusion \n b) Selective inclusion \n c) Conditional compilation \n d) Recursive macros \n")
if Ans == 'c':
    print("\n Correct")
    print("+1 point \n")
    score = score + 1
else:
    print(
        "\n incorrect \n Explanation: Conditional compilation is the preprocessor facility to produce a different executable.\n")
Ans = input("4. The C-preprocessors are specified with _ symbol. \n a) # \n b) $ \n c) ” ” \n d) & \n ")
if Ans == 'a':
    print("\n Correct")
    print("+1 point \n")
    score = score + 1
else:
    print("\n incorrect \n Explanation: The C-preprocessors are specified with # symbol.\n")
Ans = input(
    "5.Which of the following is not an operator in C? \n a) , \n b) sizeof() \n c) ~ \nd) None of the mentioned \n")
if Ans == 'd':
    print("\n Correct")
    print("+1 point\n")
    score = score + 1
else:
    print("\nincorrect \n none ")
print("Total score is", score)