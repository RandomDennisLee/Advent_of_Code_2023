import re


def check_color(pattern: re.Pattern):
    largest_number = 0
    all_instances = pattern.findall(line)
    for string in all_instances:
        for token in string.split():
            if token.isnumeric():
                if int(token) > largest_number:
                    largest_number = int(token)
    return largest_number


if __name__ == '__main__':
    red = re.compile(r'\d*\sred')
    green = re.compile(r'\d*\sgreen')
    blue = re.compile(r'\d*\sblue')
    file = open('input.txt')
    total = 0

    for line in file:
        power = (check_color(red) *
                 check_color(green) *
                 check_color(blue))

        total += power

    print(total)
