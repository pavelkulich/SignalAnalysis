numbers = 7  # kolik chceme vypsat cislic z rady

# prvni dve cislice z rady
n1 = 0
n2 = 1

# pocitadlo iteraci
count = 0

# kontrola, zda je pocet cislic vetsi 0
if numbers <= 0:
    print("Please enter a positive integer")

# je-li pocet cislic roven 1, vypise prvni cisloci (n1)
elif numbers == 1:
    print("Fibonacci sequence with", numbers, "numbers:")
    print(n1)

# je-li pocet cislic vetsi 1 ...
else:
    print("Fibonacci sequence:")
    while count < numbers:
        print(n1)
        nth = n1 + n2

        # prepsani puvidnich hodnot
        n1 = n2
        n2 = nth

        count += 1  # zvetseni poctu iteraci; stejné jako: count = count + 1

# doplnit:
# - dynamicky uzivatelsky vstup numbers = int(input("How many output numbers? "))
# - dynamicky vstup do funkce print f"{} is positive number"
# - vytvoreni samostatne funkce
