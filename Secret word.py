counter=0
secret_word="Zoya"
while counter<7:
    word=input("Enter the secret word")
    counter=counter+1
    if word==secret_word:
        print("You guessed it right")
        break
else:
    print("Better luck next time")