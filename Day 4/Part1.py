

if __name__ == '__main__':
    data = open('input.txt').readlines()
    total = 0

    for line in data:
        winning_nos = {}
        hits = -1
        for num in line[9:40].split():
            winning_nos [num] = ''

        for num in line[40:len(line)].split():
            if num in winning_nos:
                hits += 1

        if hits > -1:
            total += pow (2, hits)

    print (total)
