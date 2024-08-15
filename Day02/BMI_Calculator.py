#BMI calculator project
weight = input("Enter Your Weight :")
height = input("Enter Your Height :")

weight_int = int(weight)
height_int = float(height)

bmi = weight_int / (height_int ** 2)

bmi_int = int(bmi)

print("bmi is :"+str(bmi_int))