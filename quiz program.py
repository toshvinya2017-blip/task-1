questions=[("which fruit is yellow in colour?"),
("how many planets in our solar system?"),
("how many continents in our world?")
]
options= (("A. Apple","B. Orange","C. Mango"),
("A. 8","B. 9","C. 10"),
("A. 5","B. 6","C. 7"))

answer=("C","A","C")
guesses=[]
score=0
q_num=0

for q in questions:
    print("\n")
    print(q)
    for o in options[q_num]:
        print(o)
    guess=input("enter A,B,C: ").upper()
    guesses.append(guess)
    if guess == answer[q_num]:
        print("CORRECT!")
        score+=1
    else:
        print("INCORRECT!")
        print(f"{answer[q_num]} is the correct answer",)

    q_num+=1
print("your score is: ",score)
    
