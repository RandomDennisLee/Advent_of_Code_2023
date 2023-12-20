import math

if __name__ == '__main__':
    data = open('input.txt').readlines()
    directions = data[0].removesuffix('\n')
    locations = []
    my_map = {}
    steps_to_end = []
    steps = 0

    for line in data[2:len(data)]:
        my_map[line[0:3]] = {'L': line[7:10], 'R': line[12:15]}
        if line[2] == 'A':
            locations.append(line[0:3])

    while len(steps_to_end) != len (locations):
        for direction in directions:
            steps += 1
            for i in range (len (locations)):
                location = my_map.get(locations[i]).get(direction)

                if locations[i][2] != 'Z':
                    locations[i] = location
                    if location[2] == 'Z':
                        steps_to_end.append(steps)

            if len(steps_to_end) == len (locations):
                break

    print (math.lcm(*steps_to_end))
