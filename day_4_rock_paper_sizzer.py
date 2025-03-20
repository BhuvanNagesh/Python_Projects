import random

print("Welcome to Rock Paper Scissors!\n")

print("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissor.\n")
choice = int(input("Enter your choice!\n"))
if choice == 0 :
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif choice == 1 :
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

else  :
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


random_integer = random.randint(0, 2)
if random_integer == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

elif random_integer == 1:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

else :
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    
if choice == random_integer :
    print("We have a draw!")
elif choice == 0 and random_integer ==1 :
    print("You loose!")
elif choice == 0 and random_integer ==2 :
    print("You win!")
elif choice == 1 and random_integer ==0 :
    print("You win!")
elif choice == 1 and random_integer ==2 :
    print("You loose!")
elif choice == 2 and random_integer ==0 :
    print("You loose!")
elif choice == 2 and random_integer ==1 :
    print("You win!")
else :
    print("You gave wrong number, You loose!")


# if choice == random_integer:
#             print("We have a draw!")
#         elif (choice == 0 and random_integer == 2) or \
#              (choice == 1 and random_integer == 0) or \
#              (choice == 2 and random_integer == 1):
#             print("You win!")
#         else:
#             print("You lose!")

