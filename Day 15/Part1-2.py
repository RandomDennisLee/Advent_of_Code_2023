if __name__ == '__main__':
	data = open ('input.txt').readline ()
	total = 0
	boxes = []
	for i in range (256):
		boxes.append({})

	for string in data.split (','):
		operation = ''
		if string.endswith ('-'):
			operation = '-'
		else:
			operation = '='
		details = string.partition (operation)
		print (details)

		box = 0
		for letter in details[0]:
			box = ((box + ord (letter)) * 17) % 256
		print (box)

		if operation == '=':
			boxes[box][details[0]] = details[2]

		if operation == '-':
			if details[0] in boxes[box]:
				del (boxes[box][details[0]])

	print ('-----')
	for i in range(len(boxes)):
		if len (boxes[i]) > 0:
			print ('Box',i,boxes[i])
			lens_num = 0
			for lens in boxes[i]:
				lens_num += 1
				total += ((i+1) * lens_num * int(boxes[i][lens]))
	print (total)
