import random


my_list = ["R", "P", "S"]
user_option = input("Pick an option between R, P or S\n")
while True:
    if user_option not in my_list:
        print("!!!Invalid\nTry Again")
        user_option = input("Pick an option between R, P or S\n")
    else:
        cpu_option = random.choice(my_list)
        print(f"Player {user_option}: CPU ({cpu_option})")
        break