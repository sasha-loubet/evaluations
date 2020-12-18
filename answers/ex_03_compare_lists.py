primenumbers = open("primenumbers.txt", "r")
happynumbers = open("happynumbers.txt", "r")

happynumbers_list = happynumbers.readlines()

overlap = list()

for line in primenumbers:
	if line in happynumbers_list:
		overlap.append(line.strip() )


print (overlap)