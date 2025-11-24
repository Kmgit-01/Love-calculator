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

#Write your code below this line 👇
import random
game_images=[rock,paper,scissors]
user_choice=int(input("What do you choose?Type 0 for rock,1 for paper,2 for scisscors.\n"))
computer_choice=random.randint(0,2)
print(game_images[computer_choice])
print("\nCOMPUTER CHOOSE:")
if (user_choice>=3) or (user_choice<=0):
    print("You typed the invalid number!!!\n")
else:
    print(game_images[user_choice])
if computer_choice==0 and user_choice==1:
    print("you win")
elif computer_choice==1 and user_choice==2:
    print("you win")
elif computer_choice==2 and user_choice==0:
    print("you win")
elif computer_choice==user_choice:
    print("it's a draw")
else:
    print("you lose")
# if (user_choice>=3) or (user_choice<=0):---> Here, this code will not gonna going to work because before this code we are printing this--print(game_images[user_choice]) and in the list there are only 3 items 
#    print("You typed the invalid number!!!\n") 
