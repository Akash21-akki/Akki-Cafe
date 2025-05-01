# The Rock Paper Scissor
import random
pc = random.choice([0,1,2])
pcTurn = input("Enter your choice: ")
pcDict = {"r":0, "p":1, "s":2}
myDict = {0:'🥌', 1:'📄', 2:'✂'}
me = pcDict[pcTurn]
print(f"You chose {myDict[me]}\nPC chose {myDict[pc]}")

if (pc == me):
    print("Its Tie❌")
else:
    if(pc == 0 and me == 1): # Pc = Rock, Me = Paper 1
        print("You Win")
    elif(pc == 2 and me == 0): # Pc = Scissor, Me = Rock 2
        print("You Win")
    elif(pc == 1 and me == 2): # Pc = Paper, Me = Scissor 3
        print("You Win")
    elif(pc == 1 and me == 0): # Pc = Paper, Me = Rock 1
        print("PC Win")
    elif(pc == 0 and me == 2): # Pc = Rock, Me = Scissor 2
        print("PC Win")
    elif(pc == 2 and me == 1): # Pc = Scissor, Me = Paper 3
        print("PC Win")
    else:
        print("Something went wrong❗")

# elif((pc + me) == 1 or (pc + me) == 2 or (pc + me) == 3):
#     print("You Lose!")
# else:
#     print("You win!")