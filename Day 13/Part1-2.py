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

	def smudge (self, y, x):
		if self.contents [y] [x] == '.':
			self.contents [y] [x] = '#'
		else:
			self.contents [y] [x] = '.'

	def smudge_all (self):
		original_reflection = self.find_reflection ()
		for i in range (len (self.contents [0])):
			for j in range (len (self.contents)):
				self.smudge (j, i)
				reflection = self.find_reflection (original_reflection)
				if reflection >= 0 and reflection != original_reflection:
					print (self)
					return reflection
				self.smudge (j, i)
		print (self)

	def find_reflection (self, ignore=-1):
		reflection = self.reflect (ignore/100) * 100
		if reflection < 0:
			self.rotate ()
			reflection = self.reflect (ignore)
			self.rotate ()
		return reflection

	def reflect (self, ignore=-1):
		for reflection_point in range (len (self.contents) - 1):
			is_reflection = True
			for testing_line in range (reflection_point + 1):
				reflection_line = 2 * reflection_point - testing_line + 1
				# print ('Reflecting after line', reflection_point, ', Comparing line ', testing_line, 'to', reflection_line)
				if (reflection_point == ignore-1 or
						(reflection_line < len (self.contents) and
						 self.contents [testing_line] != self.contents [reflection_line])):
					is_reflection = False
					break

			if is_reflection:
				return reflection_point + 1
		return -1


if __name__ == '__main__':
	data = open ('input.txt').readlines ()
	total = 0

	current_puzzle = []
	for line in data:
		if len (line) > 1:
			current_line = []
			for each in line [:len (line) - 1]:
				current_line.append (each)
			current_puzzle.append (current_line)

		else:
			puzzle = Puzzle (current_puzzle)
			# print (puzzle)
			total += (puzzle.smudge_all ())
			current_puzzle = []

	print (total)
