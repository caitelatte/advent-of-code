f = open("d03-input.txt", "r")
houses = set([(0,0)])
coords = [[0,0],[0,0]]
which_santa = True
# Change changing_santa to True if looking at question 2
changing_santa = False
for line in f:
    for direction in line:
        if which_santa:
            if direction == "^":
                coords[0][1] += 1
            elif direction == "v":
                coords[0][1] -= 1
            elif direction == "<":
                coords[0][0] -= 1
            elif direction == ">":
                coords[0][0] += 1
            if (coords[0][0], coords[0][1]) not in houses:
                houses.add((coords[0][0], coords[0][1]))
            if changing_santa:
                which_santa = False
        else:
            if direction == "^":
                coords[1][1] += 1
            elif direction == "v":
                coords[1][1] -= 1
            elif direction == "<":
                coords[1][0] -= 1
            elif direction == ">":
                coords[1][0] += 1
            if (coords[1][0], coords[1][1]) not in houses:
                houses.add((coords[1][0], coords[1][1]))
            which_santa = True
print("Unique houses: " + str(len(houses)))
