import re
f = open("d05-input.txt", "r")
counter = 0
# Part 1 regex
vowel_re = re.compile(r"[aeiou].*[aeiou].*[aeiou]")
double_re = re.compile(r"(.)\1")
exclude_re = re.compile(r"ab|cd|pq|xy")
# Part 2 regex
pairs_re = re.compile(r"(..).*\1")
repeat_re = re.compile(r"(.).\1")
# Part switcher
part_one = False
for line in f:
	string = line.strip()
	if part_one:
		if vowel_re.search(string) and double_re.search(string) and (not exclude_re.search(string)):
			print("Nice string: " + string)
			counter += 1
		else:
			print(string + " didn't match:")
			if not vowel_re.search(string):
				print("  vowel " + str(vowel_re.search(string)))
			if not double_re.search(string):
				print("  doubl " + str(double_re.search(string)))
			if exclude_re.search(string):
				print("  exclu " + str(exclude_re.search(string)))
	else:
		if pairs_re.search(string) and repeat_re.search(string):
			# print ("Nice string: " + string)
			counter += 1
		else:
			print ("Naughty string: " + string, end="")
			if not pairs_re.search(string):
				print ("  pairs  " + str(pairs_re.search(string)), end="")
			else:
				print ("             ", end="")
			if not repeat_re.search(string):
				print ("  repeat  " + str(repeat_re.search(string)), end="")
			print()
print(counter)
