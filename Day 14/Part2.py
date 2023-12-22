import copy


class Puzzle:
	def __init__ (self, contents):
		self.contents = contents

	def __repr__ (self):
		result = ''
		for line in self.contents:
			for token in line:
				result += token
			result += '\n'
		return result

	def move_rock (self, y, x, direction):
		if (self.contents [y] [x] == 'O' and
				len (self.contents) > y + direction [0] >= 0 and
				len (self.contents [0]) > x + direction [1] >= 0 and
				self.contents [y + direction [0]] [x + direction [1]] == '.'):
			self.contents [y] [x] = '.'
			self.contents [y + direction [0]] [x + direction [1]] = 'O'
			self.move_rock (y + direction [0], x + direction [1], direction)

	def tilt (self, direction):
		for i in range (len (self.contents [0])):
			for j in range (len (self.contents)):
				self.move_rock (j, i, direction)
				self.move_rock (len (self.contents) - j - 1, len (self.contents [0]) - i - 1, direction)

	def spin (self):
		self.tilt ([-1, 0])
		self.tilt ([0, -1])
		self.tilt ([1, 0])
		self.tilt ([0, 1])

	def weigh (self):
		weight = 0
		for y in range (len (self.contents)):
			weight += self.contents [y].count ('O') * (len (self.contents) - y)
		return weight


if __name__ == '__main__':
	data = open ('input.txt').readlines ()
	total = 0
	history = []

	current_puzzle = []
	for line in data:
		current_line = []
		for each in line [:len (line) - 1]:
			current_line.append (each)
		current_puzzle.append (current_line)

	puzzle = Puzzle (current_puzzle)
	original_puzzle = copy.deepcopy(puzzle)
	cycles = 1000000000
	for i in range (cycles):
		i += 1
		puzzle.spin()

		print ('Cycle ', i)
		if history.count(puzzle.contents.__repr__()):
			print ('Current result found in history at cycle ', history.index(puzzle.contents.__repr__()) + 1)
			loop_size = len (history) - history.index(puzzle.contents.__repr__())
			# print ('Loop size:', loop_size)
			print (puzzle.weigh ())

			cycles = ((cycles - i) % loop_size) + i

			break
		else:
			print (puzzle.weigh ())
			history.append (puzzle.contents.__repr__ ())

	print ('Total cycles:', cycles)
	for i in range (cycles):
		original_puzzle.spin()

	print ('Weight:', original_puzzle.weigh ())
