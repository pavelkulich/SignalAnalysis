numbers = []
while True:
    line = input("zadej cele cislo: ")
    if line:
        try:
            number = int(line)
            numbers.append(number)
        except ValueError as error:
            print(error)
            print(f"{line} neni cislo")
            break

print(f"pridal jsi tato cisla: {numbers}")