number = 7
factorial = 1

# je cislo mensi nez 0?
if number < 0:
    print("Sorry, factorial does not exist for negative numbers")

elif number == 0:
    print("The factorial of 0 is 1")

else:
    for i in range(1, number + 1):
        factorial = factorial * i

    print("The factorial of", number, "is", factorial)

# doplnit:
# - dynamicky uzivatelsky vstup userInput = input("Enter a number: ")
# - dynamicky vstup do funkce print f"{} is positive number"
# - vytvoreni samostatne funkce
