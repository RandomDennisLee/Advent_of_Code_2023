def find_min_charge_time(total_time, distance_to_beat, time_range_start, time_range_end):
    charge_time = int ((time_range_start + time_range_end)/2)

    if (time_range_end - time_range_start) == 1:
        return time_range_start if check_distance(total_time, time_range_start, distance_to_beat) else time_range_end

    if check_distance(total_time, charge_time, distance_to_beat):
        return find_min_charge_time(total_time, distance_to_beat, time_range_start, charge_time)
    else:
        return find_min_charge_time(total_time, distance_to_beat, charge_time, time_range_end)


def check_distance (total_time: int, charge_time: int, distance_to_beat):
    # print ('Charging for:', charge_time, ' secs. Distance is:', (total_time - charge_time) * charge_time)
    return (total_time - charge_time) * charge_time > distance_to_beat


if __name__ == '__main__':
    data = open('input.txt').readlines()
    times = []
    distances = []

    for token in data[0][10:].split():
        times.append (int(token))
    for token in data[1][10:].split():
        distances.append (int(token))

    # print (times, distances)
    result = 1

    for i in range(len(times)):
        ways_to_win = times[i] - 2 * find_min_charge_time(times[i], distances[i], 0, times[i]) + 1
        print ('Ways to win:', ways_to_win)
        result *= ways_to_win

    print (result)


