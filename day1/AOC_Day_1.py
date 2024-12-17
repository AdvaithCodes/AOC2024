#https://adventofcode.com/2024/day/1

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

list_1.sort()
list_2.sort()

distance = 0

for n1, n2 in zip(list_1, list_2):
    distance = distance + abs(n1 - n2)
    
print(distance)
    