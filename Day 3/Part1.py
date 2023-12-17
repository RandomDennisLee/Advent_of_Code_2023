import re


def checkline(_numbers, line):
    index = 0
    for num in _numbers:
        index = line[index:len(line)].find(num)
        print(previous_line[index - 1: index + len(num) + 1] + ', ', end='')

    print()


if __name__ == '__main__':
    data = open('input.txt').readlines()
    number_pattern = re.compile(r'\d+')
    symbol_pattern = re.compile(r'[^0-9.\n]')
    total = 0

    for i in range(len(data)):
        current_line = data[i]
        if i > 0:
            previous_line = data[i - 1]
        else:
            previous_line = ''
        if i == len(data) - 1:
            next_line = ''
        else:
            next_line = data[i + 1]

        print(current_line, end='')
        numbers = number_pattern.findall(current_line)

        index = 0
        for num in numbers:
            index = current_line.find(num, index) - 1
            if index < 0:
                index = 0
            if symbol_pattern.search(previous_line[index : index + len(num) + 2]) \
                    or symbol_pattern.search(current_line[index : index + len(num) + 2]) \
                    or symbol_pattern.search(next_line[index : index + len(num) + 2]):
                total += int(num)

                print (num + ' has a symbol. Current total is ' + str(total) + '. Index is ' + str(index))

            index += len(num) + 1
            print (index)

    print (total)
