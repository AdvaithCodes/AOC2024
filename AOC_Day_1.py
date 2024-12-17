#https://adventofcode.com/2024/day/1


list_1 = [3,4,2,1,3,3]
list_2 = [4,3,5,3,9,3]

list_1.sort()
list_2.sort()

distance = 0

for n1, n2 in zip(list_1, list_2):
    distance = distance + abs(n1 - n2)
    
print(distance)
    