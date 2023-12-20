def get_endpoints (position):
    if sanity_check(position):
        return [position, position]
    direction = get_pipe(position)
    endpoints = [[position[0] + directions.get(direction)[0][0], position[1] + directions.get(direction)[0][1]],
                 [position[0] + directions.get(direction)[1][0], position[1] + directions.get(direction)[1][1]]]
    return endpoints


def get_pipe (position):
    if sanity_check(position):
        return '.'
    return data [position[1]][position[0]]


def sanity_check (position):
    return not len(data[0]) > position[0] >= 0 and len(data) > position[1] >= 0


if __name__ == '__main__':
    data = open ('input.txt').readlines()
    position = [-1, -1]
    last_position = [-1, -1]
    start_position = [-1, -1]
    total_length = 1
    directions = {'|' : [[0,1], [0,-1]],
                  '-' : [[1,0], [-1,0]],
                  '7' : [[-1,0], [0,1]],
                  'F' : [[1,0], [0,1]],
                  'J' : [[0,-1], [-1,0]],
                  'L' : [[1,0], [0,-1]],
                  '.' : [[0,0], [0,0]]}

    for i in range(len(data)):
        if data[i-1].find('S') != -1:
            start_position = [data[i-1].find('S'), i-1]

    print (start_position, get_pipe(start_position))

    neighbor1 = [start_position[0] - 1, start_position[1]]
    neighbor2 = [start_position[0] + 1, start_position[1]]
    neighbor3 = [start_position[0], start_position[1] - 1]

    if get_endpoints (neighbor1).count(start_position) == 1:
        position = neighbor1
    elif get_endpoints (neighbor2).count(start_position) == 1:
        position = neighbor2
    elif get_endpoints (neighbor3).count(start_position) == 1:
        position = neighbor3
    else:
        print ('Start link not found')

    last_position = start_position
    while position != start_position:
        print (position)
        total_length += 1

        next_position = get_endpoints(position)
        next_position.remove (last_position)
        last_position = position
        position = next_position[0]

    print (total_length/2)
