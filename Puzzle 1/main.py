if __name__ == '__main__':
    file = open ('input.txt')
    total = 0

    for line in file:
        digits = ''
        for char in line:
            if char.isdigit():
                digits = char
                break

        for char in reversed(line):
            if char.isdigit():
                digits += char
                break

        total += int(digits)

    print (total)
