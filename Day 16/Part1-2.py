import copy
import sys


class Beam:
	def __init__ (self, pos, direction):
		self.position = copy.deepcopy(pos)
		self.direction = copy.deepcopy(direction)
		self.move ()

	def move (self):
		if self.direction == 'N':
			self.position ['y'] -= 1
		if self.direction == 'S':
			self.position ['y'] += 1
		if self.direction == 'E':
			self.position ['x'] += 1
		if self.direction == 'W':
			self.position ['x'] -= 1

		x = self.position ['x']
		y = self.position ['y']

		if len (tiles [0]) > x >= 0 and len (tiles) > y >= 0:
			tile = tiles [y] [x]
			if not tile.directions [self.direction]:
				tile.activate (self.direction)

				if tile.content == '/':
					if self.direction == 'N':
						self.direction = 'E'
					elif self.direction == 'S':
						self.direction = 'W'
					elif self.direction == 'E':
						self.direction = 'N'
					elif self.direction == 'W':
						self.direction = 'S'
				if tile.content == '\\':
					if self.direction == 'N':
						self.direction = 'W'
					elif self.direction == 'S':
						self.direction = 'E'
					elif self.direction == 'E':
						self.direction = 'S'
					elif self.direction == 'W':
						self.direction = 'N'

				if tile.content == '-' and (self.direction == 'N' or self.direction == 'S'):
					self.direction = 'E'
					Beam (self.position, 'W')
				if tile.content == '|' and (self.direction == 'E' or self.direction == 'W'):
					self.direction = 'N'
					Beam (self.position, 'S')

				self.move ()


class Tile:
	def __init__ (self, con='.'):
		self.content = con
		self.directions = {'N': False,
		                   'S': False,
		                   'E': False,
		                   'W': False}
		self.activated = 0

	def activate (self, direction):
		self.directions [direction] = True
		self.activated += 1

	def __repr__ (self):
		if self.activated == 0:
			return self.content
		else:
			return str (self.activated)


def count_energized(tiles):
	energized = 0
	for row in tiles:
		for column in row:
			#print(column,end='')
			if column.activated > 0:
				energized += 1
		#print ()
	return energized


if __name__ == '__main__':
	sys.setrecursionlimit(100000)
	data = open ('input.txt').readlines ()
	tiles = []

	for line in data:
		current_line = []
		for each in line [:len (line) - 1]:
			current_line.append (Tile (each))
		tiles.append (current_line)

	ori_tiles = copy.deepcopy(tiles)

	max_energized = 0
	for i in range(len(tiles)):
		Beam ({'x': -1, 'y': i}, 'E')
		energized = count_energized(tiles)
		max_energized = energized if energized > max_energized else max_energized
		tiles = copy.deepcopy(ori_tiles)

		Beam ({'x': len(tiles[0]), 'y': i}, 'W')
		energized = count_energized(tiles)
		max_energized = energized if energized > max_energized else max_energized
		tiles = copy.deepcopy(ori_tiles)

	for i in range(len(tiles[0])):
		Beam ({'x': i, 'y': -1}, 'S')
		energized = count_energized(tiles)
		max_energized = energized if energized > max_energized else max_energized
		tiles = copy.deepcopy(ori_tiles)

		Beam ({'x': i, 'y': len(tiles)}, 'N')
		energized = count_energized(tiles)
		max_energized = energized if energized > max_energized else max_energized
		tiles = copy.deepcopy(ori_tiles)


	print (max_energized)
