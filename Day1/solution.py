
def naive(numbers_list, k):
    '''
    The naive solution loops through the array two times
    :param numbers_list: the list of numbers
    :param k: the sum of numbers
    :return: a boolean representing whether the pair exists
    '''
    for first_num in numbers_list:
        for second_num in numbers_list:
            if first_num+second_num == k:
                return True

    return False


sum_map = {}
def sum_exists(numbers_list, k):
    '''
    Returns whether a sum of numbers exists in the list
    :param numbers_list:
    :param k:
    :param n: number of items in the sum
    :return:
    '''
    global sum_map

    while True:
        if len(numbers_list) == 0:
            return False
        curr_number = numbers_list.pop()
        if k-curr_number in sum_map:
            return True
        sum_map[curr_number] = True

def dynamic(numbers_list, k):
    return sum_exists(numbers_list, k)

def dtest_solution():
    test_cases = [
        ([10, 15, 3, 7], 17),
        ([], 3),
        ([5, 4, -7, -10], -6),
        ([5,4,3,2], 100)
    ]

    for case in test_cases:
        print('Case: ')
        print(case[0])
        print("sum: %i" % case[1])
        print(dynamic(case[0], case[1]))
        print("===========")






if __name__ == "__main__":
    dtest_solution()