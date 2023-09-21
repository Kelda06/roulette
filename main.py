import random
repeat = "Yes bcs I'am gambler"
cash = int(input("Enter the amount with which you will bet in roulette: "))
while repeat == "Yes bcs I'am gambler":
    

    print("Your current available amount is: ")
    print(cash)

    num = random.randint(1, 37)
    if num == 37:
        clr = "green"

    else:
        if num % 2 == 1:
            clr = "red"

        elif num % 2 == 0:
            clr = "black"


    print(clr)
    s_c = (input("Choose color you want to bet on (red or black): "))
    s_a = int(input("Choose ammount you want to bet: "))

    if s_a > cash:
        print("You are brokie hahaha!")
        break

    print("The color is " + clr)

    if s_c == clr:
        cash = cash + s_a
        print("You have lucky... Your current ammount is: ")
        print(cash)
    else:
        cash = cash - s_a
        print("You lost your bet looser! Your current ammount is: ")
        print(cash)




    repeat = (input("Next chance?  (Yes bcs I'am gambler/No bcs I'am smart) "))
