def jian_dui(heap, start, n):
    f_index = (n - 1) // 2
    for i in range(f_index, -1, -1):
        while True:
            j = 2 * i + 1
            if j < n - 1 and heap[j] < heap[j + 1]:
                j += 1
            if j < n and heap[i] < heap[j]:
                heap[i], heap[j] = heap[j], heap[i]
            else:
                break
            i = j


def heap_sort(heap):
    n = len(heap)
    # 第一步，建堆
    jian_dui(heap, 0, n)
    while n >= 1:
        heap[0], heap[n - 1] = heap[n - 1], heap[0]
        n -= 1
        # 第二步，重新建堆
        jian_dui(heap, 0, n)
    print(heap)


import random

# heap = list(range(10))
# random.shuffle(heap)
# print(heap)
heap = [8, 5, 7, 9, 2, 10, 1, 4, 6, 3]
heap_sort(heap)
