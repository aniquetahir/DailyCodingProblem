

def find_missing_positive(numbers_array):
    least_num = 0

    # Find least positive number
    for number in numbers_array:
        if number>0 and (number<least_num or least_num == 0):
            least_num = number

    for number in numbers_array:
        if number==least_num+1:
            least_num = number

    if least_num == 0:
        return 1
    else:
        return least_num + 1

def test_solution():
    cases = [
        ([3, 4, -1, 1],2),
        ([1, 2, 0],3)
    ]

    for case, solution in cases:
        assert find_missing_positive(case)==solution

