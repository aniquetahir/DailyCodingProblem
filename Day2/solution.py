def naive(numbers_list):
    product = 1
    for number in numbers_list:
        product *= number

    return [int(product/x) for x in numbers_list]

# key = (set of indices)
# value = product
product_map = {}
def rec_product(numbers_list, starting_index, ending_index):
    global product_map
    # Base Cases
    if ending_index<0 or starting_index>=len(numbers_list):
        return 1

    if (starting_index, ending_index) in product_map:
        return product_map[(starting_index, ending_index)]

    if starting_index == ending_index:
        product_map[(starting_index, ending_index)] = numbers_list[starting_index]
        return numbers_list[starting_index]

    # No Base Cases match
    product = rec_product(numbers_list, starting_index, starting_index) * rec_product(numbers_list, starting_index+1, ending_index)
    product_map[(starting_index, ending_index)] = product

    return product

def no_div(numbers_list):
    '''
    Uses the recursive function `rec_product` to calculate the solution
    :param numbers_list:
    :return:
    '''
    global product_map
    product_map = {}
    solution = [rec_product(numbers_list, 0, i-1)*rec_product(numbers_list, i+1, len(numbers_list)-1)
                for i,x in enumerate(numbers_list)]
    return solution

def no_div_alter(numbers_list):
    '''
    O(n^2) solution that doesn't use division
    :param numbers_list:
    :return:
    '''
    solution = []
    for i, number in enumerate(numbers_list):
        product = 1
        for j, product_number in enumerate(numbers_list):
            if i != j:
                product *= product_number
        solution.append(product)
    return solution

def dtest_solution():
    test_cases = [
        ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
        ([3, 2, 1], [2, 3, 6]),
        ([],[])
    ]

    for test_case, solution in test_cases:
        print('Expected output: ')
        print(solution)
        print('Your output: ')
        print(no_div_alter(test_case))
        print('==============')


if __name__ == "__main__":
    dtest_solution()