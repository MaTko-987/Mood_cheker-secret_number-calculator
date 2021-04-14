plus = "+"

minus = "-"

divide = "/"

multiply = "*"

user_input = print("Today we are learning math! Good luck!")

user_input1 = int(input("Input your first number: "))

user_input2 = input("Input your operation sign(+,-,/,*): ")

user_input3 = int(input("Input your second number: "))



if user_input2 == plus:
    print(user_input1 + user_input3)

elif user_input2 == minus:
    print(user_input1 - user_input3)

elif user_input2 == divide:
    print(user_input1 / user_input3)

elif user_input2 == multiply:
    print(user_input1 * user_input3)

else:
    print("Something went wrong. Try again!")


