print('''  |\__/|
          /     \
         /_.~ ~,_\   
            \@/''')
print("Welcome to Treasure Island game")
direction = input("where you want to go left or right\n").lower()

if direction=="right":
    lake = input("you are now near lake you want to swim or wait").lower()
    if lake == "swim":
         door = input("you passed this lake now you have to choose door among three doors 1.red 2.black 3.blue").lower()
         if door == "red":
            print("Game over Better luck next time !!!")
         elif door == "black":
            print("Yeeeeeeeyy you Win !!!")
         else:
            print("Game Over Better Luck Next Time")
    else:
       print("Game Over !!! you were attacked by animals")
else :
    print("Game Over")
