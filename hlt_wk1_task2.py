# Number Guessing Game
joke1 = (" I failed math so many times at school, I can’t even count. ")
joke2 = ("Don’t you hate it when someone answers their own questions? I do. ")
joke3 = ("I know they say that money talks, but all mine says is ‘Goodbye.’ ")
number_guess = int(input ("Type a Number Between 1 to 100: "))
if number_guess <= 30:
    print(joke1)
elif  30 < number_guess <= 60:
    print(joke2)
elif 60 < number_guess <= 100:
    print(joke3)
else:
    print("Your chosen number is not within the range")



