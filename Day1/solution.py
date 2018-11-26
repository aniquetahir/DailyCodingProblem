import heapq

def merge(lists):
    merged_list = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)

        merged_list.append(val)

        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1],
                          list_ind,
                          element_ind + 1)
            heapq.heappush(heap, next_tuple)
    return merged_list

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