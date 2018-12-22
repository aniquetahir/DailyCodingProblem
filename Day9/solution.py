from collections import defaultdict

def get_max_sum(num_list):
    if len(num_list) == 0:
        return 0

    if len(num_list)<3:
        return max(num_list)

    list_size = len(num_list)

    memoized_left_sum = defaultdict(int)

    for i in range(list_size):
        memoized_left_sum[i] = max( memoized_left_sum[i-2] + num_list[i], memoized_left_sum[i-1] )

    return memoized_left_sum[list_size-1]

def test_solution():
    test_cases = [
        ([2, 4, 6, 2, 5],13),
        ([5, 1, 1, 5],10),
        ([1,2,3,4],6),
        ([4,3,2,1],6)
    ]

    for case in test_cases:
        assert get_max_sum(case[0])==case[1]





