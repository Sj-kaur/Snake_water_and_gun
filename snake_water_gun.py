import random

print("WELCOME TO SNAKE , WATER AND GUN GAME")
lst=['s','w','g']
computer = random.choice(lst)
print("Number of chances to play this game is 10")
chance = 1
count1 = 0  # here count1 is for computer
count2 = 0   # here count2 is foor user
ties = 0
while chance<=10:
    user = input("Choose any one : \n s for snake \n w for water \n g for gun")
    if user == computer:
        print("tie between user and computer ")
        ties = ties + 1
    elif (computer == 's' and user == 'w') or (computer == 'w' and user == "g") and (computer == 'g' and user == 's'):
        print("Computer win this round")
        count1 = count1 + 1
    elif (computer == 'w' and user == 's') or (computer == 'g' and user == 'w') or (computer == 's' and user == 'g'):
        print("You win this round ")
        count2 = count2 + 1
    chance = chance + 1
print("Number of times the computer win = ", count1)
print("Number of times you win = ", count2)
print("Number of ties = ",ties)
if count1 == count2:
    print("There is a tie")
elif count1>count2:
    print("YOU LOSE, COMPUTER WINS")
else:
    print("CONGRATULATIONS, YOU WIN")

