# #pirate Treasure Game 
# list1 = ["","",""]
# list2 = ["","",""]
# list3 = ["","",""]
# map = [list1,list2,list3]
# print("where you want to hide this treasure?")
# position = input()
# letter = position[0].lower()

# abc  = ["a","b","c"]
# letter_index = abc.index[letter]
# print(letter_index)
# number_index = int(position[1])-1
# print(number_index)
# map[letter_index][number_index] = "x"



# Pirate Treasure Game
list1 = ["", "", ""]
list2 = ["", "", ""]
list3 = ["", "", ""]
map = [list1, list2, list3]

print("Where do you want to hide this treasure? (e.g., a1, b2)")
position = input()
letter = position[0].lower()

abc = ["a", "b", "c"]
letter_index = abc.index(letter)
print("Letter index:", letter_index)

number_index = int(position[1]) - 1
print("Number index:", number_index)

map[letter_index][number_index] = "x"

# Printing the map to show the treasure location
for row in map:
    print(row)
