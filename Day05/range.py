#fizz and buzz range exercise
for numb in range(0,101):
   
    if(numb != 0 and numb % 3 == 0):
        print("buzz")
    elif(numb != 0 and numb % 5 == 0):   
        print("fizz")
    else:
        print(numb)