import re


def check_color(pattern: re.Pattern, limit: int):
    all_instances = pattern.findall(line)
    for string in all_instances:
        for token in string.split():
            if token.isnumeric():
                if int(token) > limit:
                    return False
    return True


if __name__ == '__main__':
    red = re.compile(r'\d*\sred')
    green = re.compile(r'\d*\sgreen')
    blue = re.compile(r'\d*\sblue')
    file = open('input.txt')
    total = 0
    game_id = 1

    for line in file:
        success = (check_color(red, 12) and
                   check_color(green, 13) and
                   check_color(blue, 14))

        if success:
            total += game_id

        game_id += 1

    print (total)
