f = open("d01-input.txt", "r")
floor = 0
char = 1
for line in f:
	for bracket in line:
		if bracket == "(":
			floor += 1
		elif bracket == ")":
			floor -= 1
		# comment out this if if looking for the first half of the question
		if floor < 0:
			print(char)
			break
		char += 1
print(floor)