'''
             2
       4          5
    9     6    7     8
  11 16 (1)
'''


def up_to_heap(heap, num):
    n = len(heap)
    heap.append(num)
    f_index = n
    while f_index > 0:
        c_index = (f_index - 1) // 2
        if heap[f_index] < heap[c_index]:
            heap[f_index], heap[c_index] = heap[c_index], heap[f_index]
        f_index = c_index
    print(heap)


"""
             8           
       5          7
    9     2    10    1
  4  6  3 (11)
"""


def dowm_to_heap(heap, num):
    n = len(heap)
    heap.append(num)
    f_index = (n - 1) // 2
    for i in range(f_index, -1, -1):
        while True:
            j = 2 * i + 1
            if j < n - 1 and heap[j] > heap[j + 1]:
                j += 1
            if j < n and heap[i] > heap[j]:
                heap[i], heap[j] = heap[j], heap[i]
            else:
                break
            i = j

    print(heap)


if __name__ == '__main__':
    # heap = [2, 4, 5, 9, 6, 7, 8, 11, 16]
    # up_to_heap(heap, 1)

    heap = [8, 5, 7, 9, 2, 10, 1, 4, 6, 3]
    dowm_to_heap(heap, 11)
