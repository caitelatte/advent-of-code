f = open("d06-input.txt", "r")
lights = {}
part_one = False
for line in f:
	line = line.strip().replace("turn ", "turn").split(" ")
	coords1 = line[1].split(",")
	coords2 = line[3].split(",")
	if part_one:
		if line[0] == "turnon":
			for x in range(int(coords1[0]), int(coords2[0]) + 1):
				for y in range(int(coords1[1]), int(coords2[1]) + 1):
					lights[(x, y)] = True
		elif line[0] == "turnoff":
			for x in range(int(coords1[0]), int(coords2[0]) + 1):
				for y in range(int(coords1[1]), int(coords2[1]) + 1):
					if (x,y) in lights:
						del lights[(x, y)]
		elif line[0] == "toggle":
			for x in range(int(coords1[0]), int(coords2[0]) + 1):
				for y in range(int(coords1[1]), int(coords2[1]) + 1):
					if (x,y) in lights:
						del lights[(x,y)]
					else:
						lights[(x,y)] = True
	else:
		if line[0] == "turnon":
			for x in range(int(coords1[0]), int(coords2[0]) + 1):
				for y in range(int(coords1[1]), int(coords2[1]) + 1):
					if (x,y) in lights:
						lights[(x,y)] += 1
					else:
						lights[(x,y)] = 1
		elif line[0] == "turnoff":
			for x in range(int(coords1[0]), int(coords2[0]) + 1):
				for y in range(int(coords1[1]), int(coords2[1]) + 1):
					if (x,y) in lights:
						if lights[(x,y)] > 0:
							lights[(x,y)] -= 1
		elif line[0] == "toggle":
			for x in range(int(coords1[0]), int(coords2[0]) + 1):
				for y in range(int(coords1[1]), int(coords2[1]) + 1):
					if (x,y) in lights:
						lights[(x,y)] += 2
					else:
						lights[(x,y)] = 2
print("Part One (len): " + str(len(lights)))
print("Part Two (sum): " + str(sum(lights.values())))
