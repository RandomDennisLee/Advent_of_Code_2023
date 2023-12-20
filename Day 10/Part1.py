
if __name__ == '__main__':
    data = open ('input.txt').readlines()
    position = [-1, -1]
    start_position = [-1, -1]
    directions = {'|':[[0,1], [0,-1]],
                  '-':[[1,0], [-1,0]],
                  '7'}

    for i in range(len(data)):
        if data[i-1].find('S') != -1:
            start_position = [i-1, data[i-1].find('S')]

    print (start_position, data[start_position[0]][start_position[1]])