#https://adventofcode.com/2024/day/2

def generate_list_from_file(filename, isNumbers=False):
    with open(filename, 'r') as file:
        lines = file.readlines()
        generated_list = []
        for x in lines:
            value = x.strip()
            if isNumbers:
                generated_list.append(int(value))
            else:
                generated_list.append(value)
    return generated_list

def all_same_sign(lst):
    """Checks if all values in a list are either greater than 0 or less than 0.

    Args:
        lst: The list to check.

    Returns:
        True if all values are either greater than 0 or less than 0, False otherwise.
    """

    if len(lst) == 0:
        return True

    first_value = lst[0]
    for value in lst:
        if value * first_value <= 0:
            return False
    return True


# ["58 59 62 63 64 63", "71 72 74 76 78 80 82 82", "26 29 32 34 35 39", "9 11 14 17 19 20 21 26"]
def check_ok(inputList):
    list_of_lists = [[int(num) for num in string_of_numbers.split()] for string_of_numbers in inputList]
    #print(list_of_lists) #[[58, 59, 62, 63, 64, 63],[58, 59, 62, 63, 64, 63],[58, 59, 62, 63, 64, 63]..]

    success_count = 0

    for i in range(len(list_of_lists)): #0 to 5...
        current_list = list_of_lists[i]
        intervals = []
        for i in range(len(current_list) - 1): 
            interval = current_list[i + 1] - current_list[i]
            intervals.append(interval)
        #print(intervals)
        #cdprint(current_list)
        #print(intervals)
        #distance = abs(interval)
        results = []

        #[-1, -2, -2, -1]
        if all_same_sign(intervals):
            #then proceed to other checks
            for num in intervals:
                if abs(num) > 0 and abs(num) <=3:
                    results.append(True)
                    #print("true")          
                else:
                    results.append(False)
                    #print("false")
        else:
            results.append(False) # reject entire list with a single False

        if all(results) == True:
            success_count += 1 

    print(success_count)


myList = generate_list_from_file('day2-list1.txt')
check_ok(myList)