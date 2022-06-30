#!/usr/bin/env1 python3
  
# Seasons and Cities
locations = ["Denver, CO", "Dallas, TX", "Seattle, WA", "Boston, MA"]
budget = [787, 1091, 1220, 1419]

keep_going = True

print("Please pick a 1-4 for a vacation recommendation.")

def calculate_budget(user_input):
    if (user_input == "1"):
        print(f"We recommend ${str(budget[0])} for a one person budget or ${str(budget[0] * 2)} for two people.")
    elif (user_input == "2"):
        print(f"We recommend ${str(budget[1])} for a one person budget or ${str(budget[1] * 2)} for two people.")
    elif (user_input == "3"):
        print(f"We recommend ${str(budget[2])} for a one person budget or ${str(budget[2] * 2)} for two people.")
    elif (user_input == "4"):
        print(f"We recommend ${str(budget[3])} for a one person budget or ${str(budget[3] * 2)} for two people.")

while(keep_going):
    user_input = input("Please pick a season: \n1: Winter \n2: Spring \n3: Summer \n4: Fall\n")
    if (user_input == "1"):
        print(f"We recommend {locations[0]} for your vacation!\n")
        calculate_budget(user_input)
        answer = input("would you like to pick another location? y or n:\n")
        if (answer == "y"):
            keep_going
        elif (answer == "n"):
            print("GoodBye!")
            keep_going = False
        else:
            print("Please enter y or n")
    elif (user_input == "2"):
        print(f"We recommend {locations[1]} for your vacation!\n")
        calculate_budget(user_input)
        answer = input("would you like to pick another location? y or n:\n")
        if (answer == "y"):
            keep_going
        elif (answer == "n"):
            print("GoodBye!")
            keep_going = False
        else:
            print("Please enter y or n")
    elif (user_input == "3"):
        print(f"We recommend {locations[2]} for your vacation!\n")
        calculate_budget(user_input)
        answer = input("would you like to pick another location? y or n:\n")
        if (answer == "y"):
            keep_going
        elif (answer == "n"):
            print("GoodBye!")
            keep_going = False
        else:
            print("Please enter y or n")
    elif (user_input == "4"):
        print(f"We recommend {locations[3]} for your vacation!\n")
        calculate_budget(user_input)
        answer = input("would you like to pick another location? y or n:\n")
        if (answer == "y"):
            keep_going
        elif (answer == "n"):
            print("GoodBye!")
            keep_going = False
        else:
            print("Please enter y or n")
    else:
        print("That is an invalid input please try again\n")
