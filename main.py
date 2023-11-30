import random
import sys

import my_module

# random_integer = random.randint(0, 5)
# print(random_integer)

# print(my_module.pi)

# random_float = random.random()
# print(random_float)

# print(random_integer * random_float)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}.")

# / # / # EXERCISE # / # / #

# import random

# heads_tails = random.randint(0, 1)

# if heads_tails == 0:
#     print("Tails")
# else:
#     print("Heads")

# / # / # / # / # / #

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
#                      "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
#                      "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
#                      "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
#                      "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
#                      "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
#                      "New Mexico", "Arizona", "Alaska", "Hawaii"]

# states_of_america[31] = "Mini Soda"

# states_of_america.append("Center Dakota")
# states_of_america.extend(["North Alaska", "South Hawaii"])

# num_of_states = len(states_of_america)

# print(states_of_america[num_of_states - 1])

# / # / # EXERCISE # / # / #

# import random

# names_string = "Angela, Ben, Jenny, Michael, Chloe"
# names = names_string.split(", ")
# items = len(names)
# random_number = random.randint(0, items - 1)

# print(f"{names[random_number]} is going to buy the meal today!")

# / # / # / # / # / #

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",
#                "Tomatoes", "Celery", "Potatoes"]

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery",
#           "Potatoes"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen)

# / # / # EXERCISE # / # / #

# line1 = ["⬜️", "️⬜️", "️⬜️"]
# line2 = ["⬜️", "⬜️", "⬜️"]
# line3 = ["⬜️", "⬜️", "⬜️"]

# treasure_map = [line1, line2, line3]

# print("Hiding your treasure! X marks the spot.")

# position = input("Where do you want to put the treasure? ")

# abc = ["A", "B", "C"]
# x_data = int(position[1])
# y_data = position[0].upper()

# x_coordinate = x_data - 1
# y_coordinate = abc.index(y_data)

# treasure_map[x_coordinate][y_coordinate] = "❌"

# print(f"{line1}\n{line2}\n{line3}")

# / # / # / # / # / #

# / # / # PROJECT OF DAY 4 # / # / #

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

r_p_s = [rock, paper, scissors]
computer_choice = random.randint(0, 2)

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice >= 3 or choice < 0:
    print("No flamethrowers or magic wands here!")
#     sys.exit(0)
else:
    print(r_p_s[choice])

    print(f"Computer chose:\n{r_p_s[computer_choice]}")

    if choice == 0 and computer_choice == 1:
        print("You lose!")
    elif choice == 0 and computer_choice == 2:
        print("You win!")
    elif choice == 1 and computer_choice == 0:
        print("You win!")
    elif choice == 1 and computer_choice == 2:
        print("You lose!")
    elif choice == 2 and computer_choice == 0:
        print("You lose!")
    elif choice == 2 and computer_choice == 1:
        print("You win!")
    else:
        print("It's a draw!")
