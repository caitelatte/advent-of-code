f = open("d02-input.txt", "r")
paper = 0
ribbon = 0
for box in f:
	dimensions = box.strip().split("x")
	dimensions = [int(x) for x in dimensions]
	l = dimensions[0]
	w = dimensions[1]
	h = dimensions[2]
	# Part 1 - paper = each face + minimum face
	lw = l * w
	lh = l * h
	wh = w * h
	paper += 2 * (lw + lh + wh) + min(lw, lh, wh)
	# Part 2 - ribbon = smallest perimeter + volume
	ribbon += min(2*l + 2*w, 2*l + 2*h, 2*w + 2*h) + (l * w * h)
print("Paper: " + str(paper))
print("Ribbon: " + str(ribbon))
