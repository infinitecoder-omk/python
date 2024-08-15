# Advanced BMI calculator project
weight = input("Enter Your Weight :")
height = input("Enter Your Height :")

weight_int = int(weight)
height_int = float(height) #height in meters

bmi = weight_int / (height_int * height_int)

print("bmi is :"+str(bmi))

if bmi<18:
 print(f"your bmi is :{bmi} & you are underweight !!!")
elif bmi < 25:
 print(f"your bmi is :{bmi} & you are normal !!!")
elif bmi < 28:
 print(f"your bmi is :{bmi} & you are slightly overweight !!!")
elif bmi < 30:
 print(f"your bmi is :{bmi} & you are obese !!!")
else:
 print(f"your bmi is :{bmi} & you are clinically obese !!!")