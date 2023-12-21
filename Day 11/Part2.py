import copy


class Universe:
	def __init__(self, data):
		self.expanded_row_value = 1000000
		self.contents = []
		self.locations = []
		self.expanded_rows = []
		self.expanded_columns = []
		for i in range (len (data)):
			self.contents.append ([])
			for j in range (len (data [i]) - 1):
				self.contents [i].append (data [i] [j])

	def expand_universe (self):
		self.expanded_rows = self.expand_rows ()
		self.rotate_universe ()
		self.expanded_columns = self.expand_rows ()
		self.rotate_universe ()

	def expand_rows (self):
		expanded_line = []
		for i in range (len (self.contents)):
			if self.contents [i].count ('#') == 0:
				expanded_line.append (i)
		return expanded_line

	def rotate_universe (self):
		temp_uni = []

		for i in range (len (self.contents [0])):
			temp_uni.append ([])
			for j in range (len (self.contents)):
				temp_uni [i].append (self.contents [j] [i])
		self.contents = temp_uni

	def display_universe (self):
		for line in self.contents:
			for token in line:
				print (token, end='')
			print ()

	def find_galaxies (self):
		locations = []
		temp_contents = copy.deepcopy(self.contents)
		for i in range (len (temp_contents)):
			if temp_contents [i].count ('#') > 0:
				for j in range (temp_contents [i].count ('#')):
					locations.append ([i, temp_contents [i].index ('#') + j])
					temp_contents [i].remove ('#')
		self.locations = locations

	def find_distances (self):
		total = 0
		for each in self.locations.copy():
			self.locations.remove (each)
			for each2 in self.locations:
				total += abs (each [0] - each2 [0]) + abs (each [1] - each2 [1])
				for row in self.expanded_rows:
					if each2[0] > row > each[0] or each2[0] < row < each[0]:
						total += self.expanded_row_value-1
				for row in self.expanded_columns:
					if each2[1] > row > each[1] or each2[1] < row < each[1]:
						total += self.expanded_row_value-1

		return total


if __name__ == '__main__':
	data = open ('input.txt').readlines ()
	universe = Universe (data)

	universe.expand_universe()
	universe.find_galaxies()

	universe.display_universe()
	print (universe.find_distances ())
	print (universe.expanded_rows, universe.expanded_columns)
