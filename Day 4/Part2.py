

if __name__ == '__main__':
    data = open('input.txt').readlines()
    cards = []

    for i in range(len(data)):
        cards.append(1)

    for i in range(len(data)):
        line = data[i]
        winning_nos = {}
        hits = 0

        for num in line[9:40].split():
            winning_nos [num] = ''

        for num in line[40:len(line)].split():
            if num in winning_nos:
                hits += 1

        for j in range (hits):
            cards[i+j+1] = cards[i+j+1] + cards[i]

    total = 0
    for i in cards:
        total += i

    print (cards)
    print (total)

