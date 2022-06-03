import random


my_list = ["R", "P", "S"]
user_option = input(
    "Pick an option between \nR===> Rock, \nP===> Paper \nS ===> Scissors\n")
while True:
    if user_option.upper() not in my_list:
        print("!!!Invalid\nTry Again")
        user_option = input("Pick an option between R, P or S\n")
    else:
        computer = random.choice(my_list)
        print(f"Player {user_option}: CPU ({computer})")
        if (user_option.upper() == "P" and computer =="R") or (user_option.upper() == "S" and computer=="P") or (user_option.upper() == "R" and computer=="S"):
            print("Player, You win")
            break
        elif user_option.upper() == computer:
            print("Its a tie, continue to know who wins")
            user_option = input("Pick an option between R, P or S\n")
            continue
        else:
            print("Player, You lose")
        break
