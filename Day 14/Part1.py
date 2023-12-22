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

	def rotate (self):
		temp = []
		# print ('Rotating')

		for i in range (len (self.contents [0])):
			temp.append ([])
			for j in range (len (self.contents)):
				temp [i].append (self.contents [j] [i])
		self.contents = temp

	def move_rock (self, y, x):
		if self.contents [y] [x] == 'O' and y > 0 and self.contents [y-1] [x] == '.':
			self.contents [y] [x] = '.'
			self.contents [y - 1] [x] = 'O'
			self.move_rock(y-1, x)

	def tilt (self):
		for i in range (len (self.contents [0])):
			for j in range (len (self.contents)):
				self.move_rock(j, i)

	def weigh (self):
		weight = 0
		for y in range (len (self.contents)):
			weight += self.contents[y].count ('O') * (len (self.contents) - y)
		return weight


if __name__ == '__main__':
	data = open ('input.txt').readlines ()
	total = 0

	current_puzzle = []
	for line in data:
		current_line = []
		for each in line [:len (line) - 1]:
			current_line.append (each)
		current_puzzle.append (current_line)

	puzzle = Puzzle (current_puzzle)
	puzzle.tilt()
	print (puzzle)
	# total += (puzzle.smudge_all ())

	print (puzzle.weigh())
