#Random number generator
# from 1 to 10 including 1 and 10
import random
# random_number = random.randint(1,10)
# print(random_number)

#random floating point number which not includes 1

random_number_float = random.random()
print(random_number_float)

random_number_decimal = random_number_float * 5
print(random_number_decimal)

love_score = random.randint(1,100)
print(f"your love score is {love_score}")