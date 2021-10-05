import random
rand_number = random.randint(1,10)

name = input("What is your name: ")
number_random = int(input("Enter a number between 1 and 10: "))
print("Random Number from Computer is ",rand_number)
if rand_number == number_random:
    
    print(name, "you have guessed right", "well done")
else:   
    print("Better luck next time")
    
