# User Inputs Two Random Number, and chooses the arithmetic operator to apply to them
#Program calculate, and gives result

first_number = int(input("Enter First Number: "))
second_number = int(input("Enter Second Number: "))

choose_operator = input("Enter one of the following number for specific operation: 1 = add:, 2 = subtract:, 3 = multiply:, 4 = divide:, 5 = power: ")

answer = 0
if  choose_operator == '1':
    answer = first_number + second_number
elif choose_operator == '2':
    answer = first_number - second_number
elif choose_operator  == '3':
   answer = first_number * second_number
elif choose_operator  == '4':
    answer = first_number / second_number
elif choose_operator == "5":
     answer = first_number ** second_number
else:
    print("Input character is not recognized!")

print("Numbers ", first_number, "and" , second_number, "=", "{:.2f}".format(answer))