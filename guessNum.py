print("Think of a number between 1 and 100 and I'll guess it.")
count = int(input("How many guesses do I get? "))
high = 100
low = 0
b = False
while count!=0:
    if low == (high-1):
        print("Wait; how can it be both higher than", low, "and lower than", high)
        b = True
        break
    else:
        num = int((low + high) / 2)
        guess = input("Is the number higher, lower, or the same as "+str(num)+"? ")
        count -= 1
        if guess.lower() == "lower":
            high = num
        elif guess.lower() == "higher":
            low = num
        elif guess.lower() == "same":
            print("I won")
            b = True
            break
        else:
            print("enter higher, lower or same, you just burned one of my tries")
# these two lines are testing lines
# print(num)
# print(guess)
if b != True:
    x= int(input("I lost; what was the answer? "))
    if guess == "higher" and x < num:
        print("That can't be; you said it was higher than", str(num)+"!")
    elif guess == "lower" and x > num:
        print("That can't be; you said it was lower than", str(num)+"!")
    elif x==num:
        print("That can't be; you said it was not the number", num,"!")
    else:
        print("Well played!")