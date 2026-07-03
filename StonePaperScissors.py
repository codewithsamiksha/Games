import random 
option = ["stone", "paper", "scissors"]
while True:
    user = input("Enter Your Choice: ")
    computer = random.choice(option)
    print(user)
    print(computer)

    if (user == computer):
        print("Tie")

    elif(user == "stone" and computer == "scissor"):
        print("You Win.!!")
    
    elif(user == "paper" and computer == "stone"):
        print("You Win.!!")

    elif(user == "scissor" and computer == "paper"):
        print("You Win.!!")
    
    elif(computer == "Stone" and user == "scissor"):
        print("Computer Wins.!!")
    
    elif(computer == "paper" and user == "stone"):
        print("Computer Win.!!")

    elif(computer == "stone" and user == "paper"):
        print("You Win.!!")
    
    play = input("Do You Want to Play Again (yes/no) ? = ").lower()
   

    if (play !="yes"):
        print("Thank You.!!")
        break
    
