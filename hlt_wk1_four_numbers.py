#Choose four numbers
first_number = int(input("Enter First Number: "))
second_number = int(input("Enter Second Number: "))
third_number = int(input("Enter third Number: "))
fourth_number = int(input("Enter fourth Number: "))

#Put the four chosen numbers into a list
four_numbers = [first_number, second_number, third_number, fourth_number]

#Print the list
print(four_numbers)

#Write the numbers into readme1.txt, each on a seperate line
with open("readme1.txt", "w") as numbers:
    for line in four_numbers:
        numbers.write(str(line))
        numbers.write("\n") 
numbers.close()

#Append new numbers to readme1.txt
#numbers = open("readme.txt", "a")
#numbers.write("45", "56", "70")
#numbers.write("\n")
#numbers.close()

#print final output from readme1.txt
numbers = open("readme1.txt", "r")
print(numbers.read())