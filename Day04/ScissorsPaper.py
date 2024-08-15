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
scissors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
game_images = [rock,paper,scissors]
user_choice = int(input("Enter your choice 0 for rock 1 for pepper and 2 for scissors\n"))
if user_choice >= 3 or user_choice < 0  :
 {
    print("you entered invalid numbers,you lose !!!"),
    
    
 }
else :
  print(game_images[user_choice])
  computers_choice = random.randint(0,2)
  print(f"computers choice is{computers_choice}")
  print(f"computers choice is:{game_images[computers_choice]}")


    
  if computers_choice == 0 and user_choice ==2 :
    {
        print("computer won !!!")
    }
  elif user_choice == 0 and computers_choice ==2 :
    {
        print("you won !!!")
    }
  elif computers_choice > user_choice :
    {
        print("computer win!!!")
    }
  elif computers_choice < user_choice :
    {
        print("you win!!!")
    }
  elif computers_choice == user_choice :
    { 
        print("its a draw")
    }

 
