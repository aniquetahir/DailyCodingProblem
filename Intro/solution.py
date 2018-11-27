import heapq
import math

def merge(lists):
    merged_list = []

    pairs = []
    num_pairs = int(math.ceil(len(lists)/2))

    # Form pairs
    for pair_index in num_pairs:
        if num_pairs + pair_index < len(lists):
            pairs.append((lists[pair_index], lists[pair_index+num_pairs]))
        else:
            pairs.append((lists[num_pairs + pair_index]))







def run_tests():
    cases = [
        [[10, 15, 30], [12, 15, 20], [17, 20, 32]],
        [],
        [[], [], []],
        [[], [1], [1,2]],
        [[1]],
        [[1], [1, 3, 5], [1, 10, 20, 30, 40]]
    ]

    for test_case in cases:
        print("Input: ")
        print(test_case)
        print("Output: ")
        print(merge(test_case))

if __name__ == "__main__":
    run_tests()