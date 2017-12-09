import hashlib
puzzle_input = "bgvyzdsv"
x = 1
part_one = False
while True:
	hash_object = hashlib.md5((puzzle_input+str(x)).encode())
	if part_one and hash_object.hexdigest()[:5] == "00000":
		break
	elif not part_one and hash_object.hexdigest()[:6] == "000000":
		break
	x += 1
print(x)
