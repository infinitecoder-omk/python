#Rollercoaster
height = int(input("Enter your Height:"))
Total_pay = 0
if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("Enter the age:"))
    if age < 12:
        Total_pay = 5
        print("you can pay $5")
    elif age <= 18:
        Total_pay = 9
        print("you can pay $9")
    elif age <= 19:
        Total_pay = 10
        print("you can pay $10")
    else: 
        Total_pay = 13
        print("you can pay $13")  
    photo_pay = (input("Do you want photo:"))  
    if photo_pay == 'Y':
        Total_pay += 3
        print(f"your total bill is: {Total_pay}")

else:
    print("you can not ride roller coaster")    

