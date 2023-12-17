def check_map(data1, first_map_line: int, last_map_line: int, value: int):
    first_map_line -= 1
    last_map_line -= 1
    diff = -1
    saved_map_line = -1
    index = first_map_line

    for _line in data1 [first_map_line : last_map_line + 1]:
        map_in = int (_line.split().pop(1))
        map_range = int (_line.split().pop(2))

        if value >= map_in:
            if (value - map_in < diff or diff == -1) and value - map_in <= map_range:
                diff = value - map_in
                saved_map_line = index

        index += 1

    if diff > -1:
        return int(data1[saved_map_line].split().pop(0)) + diff
    else:
        return value


if __name__ == '__main__':
    data = open('input.txt').readlines()
    line = data[0]
    results = {}

    for seed in line[6:len(line)].split():
    #for seed in ['14']:
        # soil = check_map (data, 4, 5, int(seed))
        # fertilizer = check_map (data, 8, 10, soil)
        # water = check_map (data, 13, 16, fertilizer)
        # light = check_map (data, 19, 20, water)
        # temp = check_map (data, 23, 25, light)
        # humidity = check_map (data, 28, 29, temp)
        # location = check_map (data, 32, 33, humidity)
        # print (seed, soil, fertilizer, water, light, temp, humidity, location)
        #
        soil = check_map (data, 4, 21, int(seed))
        fertilizer = check_map (data, 24, 31, soil)
        water = check_map (data, 34, 68, fertilizer)
        light = check_map (data, 71, 115, water)
        temp = check_map (data, 118, 131, light)
        humidity = check_map (data, 134, 161, temp)
        location = check_map (data, 164, 174, humidity)

        results[location] = seed
        print ('Seed ' + seed + ' = location ' + str(location))

    print ('Lowest:\n ', min(results))
