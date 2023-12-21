def expand_universe (universe):
	new_line = []
	for each in universe [0]:
		new_line.append ('.')

	lines_to_insert = []
	for i in range (len (universe)):
		if universe [i].count ('#') == 0:
			lines_to_insert.append (i)

	for i in range (len (lines_to_insert)):
		universe.insert (lines_to_insert [i] + i, new_line)

	return universe


def rotate_universe (universe):
	temp_uni = []

	for i in range (len (universe [0])):
		temp_uni.append ([])
		for j in range (len (universe)):
			temp_uni [i].append (universe [j] [i])

	return temp_uni


def display_universe (universe):
	for line in universe:
		for token in line:
			print (token, end='')
		print ()


def find_galaxies (universe):
	locations = []
	for i in range (len (universe)):
		if universe [i].count ('#') > 0:
			for j in range (universe [i].count ('#')):
				locations.append ([i, universe [i].index ('#') + j])
				universe [i].remove ('#')

	return locations


def find_distances (locations):
	total = 0
	for each in locations.copy():
		locations.remove (each)
		for each2 in locations:
			total += abs (each [0] - each2 [0]) + abs (each [1] - each2 [1])

	return total


if __name__ == '__main__':
	data = open ('input.txt').readlines ()
	universe = []

	for i in range (len (data)):
		universe.append ([])
		for j in range (len (data [i]) - 1):
			universe [i].append (data [i] [j])

	universe = expand_universe (universe)
	universe = rotate_universe (universe)
	universe = expand_universe (universe)
	universe = rotate_universe (universe)

	locations = find_galaxies (universe)
	print (find_distances (locations))
