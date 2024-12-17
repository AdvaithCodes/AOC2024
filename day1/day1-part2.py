#https://adventofcode.com/2024/day/1#part2


def get_val(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()

    num_list = []

    for line in lines:
        value = line.strip()  # Remove leading/trailing whitespace
        num_list.append(int(value))

    return num_list


list_1 = get_val('day1-list1.txt')
list_2 = get_val('day1-list2.txt')

val = 0

for n in list_1:
    counter = 0
    for m in list_2:
        if n == m:
            counter += 1
    val = val + (n * counter)

print(val)