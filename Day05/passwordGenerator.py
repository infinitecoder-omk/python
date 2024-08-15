import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '\\', '|', '`', '~']

password = ''
print("Welcome to Password generator !")
nr_letters = int(input("How many letters you want in your password ?"))
nr_numbers = int(input("How many numbers you want in your password ?"))
nr_symbols = int(input("How many symbols you want in your password ?"))

# for char in range(0,nr_letters):
#   password += random.choice(letters)

# for char in range(0,nr_numbers):
#   password += random.choice(numbers)

# for char in range(0,nr_symbols):
#   password += random.choice(symbols)    

password_list = []

for char in range(0,nr_letters):
  password_list.append(random.choice(letters)) 

for char in range(0,nr_numbers):
  password_list.append(random.choice(numbers))

for char in range(0,nr_symbols):
  password_list.append(random.choice(symbols))

random.shuffle(password_list)
print(password_list)  

# mylist = ['a', 'b', 'c', 'd', 'e']
# myorder = [3, 2, 0, 1, 4]
# mylist = [mylist[i] for i in myorder]
# print(mylist)         # prints: ['d', 'c', 'a', 'b', 'e']
