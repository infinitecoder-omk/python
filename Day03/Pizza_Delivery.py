print("Welcome to Pizza Delivary application")
pizza_size = input("Enter size if pizza you want:")
Add_peppper = input("Do you want pepper:")
Extra_cheese = input("Do you want Extra cheese:")

bill = 0

if pizza_size == "s":
    bill +=15
elif pizza_size == "m":
    bill +=20
else:
    bill +=25

if pizza_size == "s" :
    if Add_peppper == "y":
           bill += 3
else:
        bill +=5

if Extra_cheese == "y":
            bill+=1

          
print(f"your total bill is {bill}")


