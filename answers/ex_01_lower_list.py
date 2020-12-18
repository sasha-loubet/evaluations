liste = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

lowest = list()

number = int(input('Donner un nombre: '))

for i in liste:
    if i < number:
        lowest.append(i)
print (lowest)
