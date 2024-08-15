names_string= ["omkar","gourav","tushar","omkara","sandesha","ashitosh"]

names_string.extend(["aditya","akshay"])
names_string.append(["rohit","karan"])
print(names_string)
import random
random_name = random.randint(0,len(names_string)-1)  
print(random_name)
print(f"the bill is to be paid by {names_string[random_name]}")

demo = "omkar,swaroop,sanjay,sarika"
family_name = demo.split(',')
print(family_name)
print(demo) 
