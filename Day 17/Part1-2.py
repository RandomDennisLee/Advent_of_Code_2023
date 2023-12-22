import copy
import sys


class Crucible:
	def __init__ (self, x=0, y=0, direction=1):
		self.x = x
		self.y = y
		self.direction = direction
		self.distance_traveled = 0
		self.heat_lost = 0
		self.directions = ['N', 'E', 'S', 'W']


	def find_naive_value(self):

		print()

	def turn(self, steer):
		if steer == 'L':
			self.direction -= 1
		if steer == 'R':
			self.direction += 1
		self.direction %= 4
		self.distance_traveled = 1

	def move (self, steer='N'):
		if steer == 'N':
			if self.distance_traveled < 3:
				self.distance_traveled += 1
			else:
				return False
		else:
			self.turn(steer)

		if self.direction == 1:
			self.y -= 1
		if self.direction == 2:
			self.x += 1
		if self.direction == 3:
			self.y += 1
		if self.direction == 4:
			self.x -= 1

		if len (tiles [0]) > self.x >= 0 and len (tiles) > self.y >= 0:
			tile = tiles [self.y] [self.x]
			self.heat_lost += tile.content
		else:
			return False
		return True


class Tile:
	def __init__ (self, con=0):
		self.content = con

	def __repr__ (self):
		return self.content


if __name__ == '__main__':
	sys.setrecursionlimit(100000)
	data = open ('input.txt').readlines ()
	tiles = []

	for line in data:
		current_line = []
		for each in line [:len (line) - 1]:
			current_line.append (Tile (int(each)))
		tiles.append (current_line)


