
if __name__ == '__main__':
    data = open('input.txt').readlines()
    directions = data[0].removesuffix('\n')
    location = 'AAA'
    my_map = {}
    steps = 0

    print (location)

    for line in data[2:len(data)]:
        my_map[line[0:3]] = {'L': line[7:10], 'R': line[12:15]}

    while location != 'ZZZ':
        for each in directions:
            location = my_map.get(location).get(each)
            print (location)
            steps += 1

            if location == 'ZZZ':
                break

    print (steps)
