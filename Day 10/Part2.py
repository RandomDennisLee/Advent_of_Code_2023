import sys


def check_neighbors (position):
    if (is_border (position) and get_pipe (position) != 'X') or get_pipe (position) == 'O':
        data [position [1]] [position [0]] = 'O'
        positions = [[position [0] - 1, position [1]], [position [0] + 1, position [1]],
                     [position [0], position [1] - 1], [position [0], position [1] + 1]]
        for each in positions:
            if not sanity_check (each) and get_pipe (each) != 'X' and get_pipe (each) != 'O':
                data [each [1]] [each [0]] = 'O'
                check_neighbors(each)

def get_endpoints (position):
    if sanity_check(position):
        return [position, position]
    direction = get_pipe(position)
    endpoints = [[position[0] + directions.get(direction)[0][0], position[1] + directions.get(direction)[0][1]],
                 [position[0] + directions.get(direction)[1][0], position[1] + directions.get(direction)[1][1]]]
    return endpoints


def get_further_endpoints (position):
    if sanity_check(position):
        return [position, position]
    direction = get_pipe(position)
    endpoints = [[position[0] + 2*directions.get(direction)[0][0], position[1] + 2*directions.get(direction)[0][1]],
                 [position[0] + 2*directions.get(direction)[1][0], position[1] + 2*directions.get(direction)[1][1]]]
    return endpoints


def get_pipe (position):
    if sanity_check(position):
        print ('panic')
        return '+'
    return data [position[1]][position[0]]


def sanity_check (position):
    result = not (len(data[0]) > position[0] >= 0 and len(data) > position[1] >= 0)
    return result


def add_pipe (position):
    for endpoint in get_endpoints(position):
        data[endpoint[1]][endpoint[0]] = 'X'
    data[position[1]][position[0]] = 'X'


def is_border (position):
    result = position[0] == 0 or position[0] == len(data[0])-1 or \
        position [1] == 0 or position [1] == len (data) - 1
    return result


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
                  '.' : [[0,0], [0,0]],
                  'S': [[0, 0], [0, 0]]}

    sys.setrecursionlimit(10000000)

    for i in range (len (data)):
        newline = []
        for j in range (len (data[i])-1):
            newline.append(data[i][j])
            newline.append('.')
        data[i] = newline

    newline = []
    for j in range (len (data[0])):
        newline.append('.')
    for i in range (len (data)):
        data.insert(len(data)-2*i, newline.copy())

    for i in range(len(data)):
        if data[i-1].count('S') > 0:
            start_position = [data[i-1].index('S'), i-1]

    print (start_position, get_pipe(start_position))

    neighbor1 = [start_position[0] - 2, start_position[1]]
    neighbor2 = [start_position[0] + 2, start_position[1]]
    neighbor3 = [start_position[0], start_position[1] - 2]

    if get_further_endpoints (neighbor1).count(start_position) == 1:
        position = neighbor1
    elif get_further_endpoints (neighbor2).count(start_position) == 1:
        position = neighbor2
    elif get_further_endpoints (neighbor3).count(start_position) == 1:
        position = neighbor3
    else:
        print ('Start link not found')

    last_position = start_position
    add_pipe(start_position)
    while position != start_position:
        total_length += 1

        next_position = get_further_endpoints(position)
        add_pipe(position)
        next_position.remove (last_position)
        last_position = position
        position = next_position[0]


    for line in data:
        for token in line:
            print (token, end='')
        print ()

    print ('---')

    for i in range (len (data)):
        for j in range (len (data [i])):
            position = [j, i]
            check_neighbors(position)

    for line in data:
        for token in line:
            print (token, end='')
        print ()

    for i in range (int (len (data)/2)):
        data.pop(i+1)
    for i in range (len (data)):
        for j in range (int (len (data[i])/2)):
            data[i].pop(j+1)

    total = len(data) * len(data[0])
    for line in data:
        total -= line.count('O')
        for token in line:
            print (token, end='')
        print ()

    total -= total_length
    print (total)
