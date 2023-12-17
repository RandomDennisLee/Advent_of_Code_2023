def find_first_num (string: str):
    index = -1
    first_num = ''

    num_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range (len(num_list)):
        num = num_list[i]
        foundIndex = string.find(num)
        if -1 < foundIndex < index or index == -1:
            index = foundIndex
            first_num = str(i+1)

    if index == -1:
        index = len(string)

    for c in string [0:index]:
        if c.isdigit():
            first_num = c
            break
    return first_num


def find_last_num (string: str):
    index = -1
    last_num = ''

    num_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range (len(num_list)):
        num = num_list[i]
        foundIndex = string.rfind(num)
        if -1 < foundIndex > index or index == -1:
            index = foundIndex
            last_num = str(i+1)

    if index == -1:
        index = 0

    for c in reversed(string [index:len(string)]):
        if c.isdigit():
            last_num = c
            break
    return last_num


if __name__ == '__main__':
    file = open ('input.txt')
    total = 0

    for line in file:
        digits = find_first_num(line)
        digits += find_last_num(line)

        total += int(digits)

    print (total)
