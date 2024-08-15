#Leap year
year = int(input("Enter a year :"))

if year % 4 == 0:
    print(f"year {year} is leap year 1")
elif year % 100 == 0:
    print(f"year {year} is not a leap year")
elif year % 400 == 0:
    print(f"year {year} is leap year")
else:
    print(f"year {year} is not a leap year")