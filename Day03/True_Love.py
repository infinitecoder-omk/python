name1 = input("Enter your name:")
name2 = input("Enter your gf name:")

combined_name = name1 + name2
combined_name = combined_name.lower()

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

score1 = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

score2 = l + o + v + e

love_score = int(str(score1) + str(score2))

if love_score <= 10 and love_score >= 90:
    print("you are like coke and mentos ...")
elif love_score <=80 and love_score >= 30:
    print("your are already in love ")
else:
    print(f"your score is {love_score}")