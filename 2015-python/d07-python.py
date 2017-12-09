wires = {} # name: value
gates = [] # [operator, x, y, output]
f = open("d07-input.txt", "r")
for line in f:
	line = line.strip().split(" -> ")
	if line[0].isdigit():
		wires[line[1]] = int(line[0])
		statement = line
	elif "AND" in line[0]:
		statement = line[0].split(" AND ")
		gates.append(["AND", statement[0], statement[1], line[1]])
	elif "LSHIFT" in line[0]:
		statement = line[0].split(" LSHIFT ")
		gates.append(["LSHIFT", statement[0], statement[1], line[1]])
	elif "RSHIFT" in line[0]:
		statement = line[0].split(" RSHIFT ")
		gates.append(["RSHIFT", statement[0], statement[1], line[1]])
	elif "NOT" in line[0]:
		statement = line[0].split("NOT ")
		gates.append(["NOT", statement[0], statement[1], line[1]])
	elif "OR" in line[0]:
		statement = line[0].split(" OR ")
		gates.append(["OR", statement[0], statement[1], line[1]])
revisit = gates
count = 0
while len(revisit) > 0:
	for gate in revisit:
		x = gate[1]
		y = gate[2]
		output = gate[3]
		if gate[0] == "AND":
			if x.isdigit():
				if y.isdigit():
					wires[output] = int(x) & int(y)
				elif y in wires:
					wires[output] = int(x) & wires[y]
				else:
					revisit.append(gate)
			elif x in wires:
				if y.isdigit():
					wires[output] = wires[x] & int(y)
				elif y in wires:
					wires[output] = wires[x] & wires[y]
				else:
					revisit.append(gate)
			else:
				revisit.append(gate)
		elif gate[0] == "LSHIFT":
			if x.isdigit():
				if y.isdigit():
					wires[output] = int(x) << int(y)
				elif y in wires:
					wires[output] = int(x) << wires[y]
				else:
					revisit.append(gate)
			elif x in wires:
				if y.isdigit():
					wires[output] = wires[x] << int(y)
				elif y in wires:
					wires[output] = wires[x] << wires[y]
				else:
					revisit.append(gate)
			else:
				revisit.append(gate)
		elif gate[0] == "RSHIFT":
			if x.isdigit():
				if y.isdigit():
					wires[output] = int(x) >> int(y)
				elif y in wires:
					wires[output] = int(x) >> wires[y]
				else:
					revisit.append(gate)
			elif x in wires:
				if y.isdigit():
					wires[output] = wires[x] >> int(y)
				elif y in wires:
					wires[output] = wires[x] >> wires[y]
				else:
					revisit.append(gate)
			else:
				revisit.append(gate)
		elif gate[0] == "NOT":
			if y.isdigit():
				wires[output] = ~ int(y)
			elif y in wires:
				wires[output] = ~ wires[y]
			else:
				revisit.append(gate)
		elif gate[0] == "OR":
			if x.isdigit():
				if y.isdigit():
					wires[output] = int(x) | int(y)
				elif y in wires:
					wires[output] = int(x) | wires[y]
				else:
					revisit.append(gate)
			elif x in wires:
				if y.isdigit():
					wires[output] = wires[x] | int(y)
				elif y in wires:
					wires[output] = wires[x] | wires[y]
				else:
					revisit.append(gate)
			else:
				revisit.append(gate)
	print("revisiting " + str(len(revisit)))
	count+=1
	if count > 3:
		break
print(wires)
print(wires["a"])