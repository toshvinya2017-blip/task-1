print("welcome to the number guessing game")
print("guess a number from 1-10")
answer=6
attempt=0

while True:

     guess=int(input("enter ur guess: "))
     attempt+=1

     if(guess>answer):
        print("too high, take another guess")

     elif(guess<answer):
        print("too low,take another guess")
     else:
        print("wohoo!!, u guessed it correct")
        print("the answer is:",answer)
        print(f"u have guessed the number in {attempt}th attempt",attempt)
        break
    


