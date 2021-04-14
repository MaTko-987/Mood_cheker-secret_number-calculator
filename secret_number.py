
secret_number1 = 56
secret_number2 = 89
secret_number3 = 12

user_input = int(input("Thank you for joining our 'Guess the secret number' game. If you guess our secert number a great prize awaits you. Your lucky number is:"))


if secret_number1 == user_input:
    print("You are our lucky winner!!!!!. 1st place wins a ferrari!!!")

elif secret_number2 == user_input:
    print("Very good!!! 2nd place wins a big screen TV!!!")

elif secret_number3 == user_input:
    print("Nice!!! 3rd place wins a tablet!!!")

else:
    print("Sorry! Try again! Good luck next time")