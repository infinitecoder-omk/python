#Day 2 Project Tip calculator
print("Welcome to pro tip calculator")

Total_Bill = float(input("Enter total bill : \n"))
Tip_percentage = int(input("Enter percentage of tip you want to give \n"))

tip = Tip_percentage /100

Add_bill = Total_Bill * tip + Total_Bill

members = (int(input("Enter Total no of members :")))

Split = float(Add_bill /members)
setplit = round(Split,2)
print(f"yor bill split is {setplit}")