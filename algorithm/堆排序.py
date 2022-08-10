def jian_dui(heap):
    n = len(heap)
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


def heap_sort(heap):
    # 第一步，建堆
    jian_dui(heap)
    result = []
    while len(heap) >= 1:
        heap[0], heap[len(heap) - 1] = heap[len(heap) - 1], heap[0]
        result.append(heap.pop())
        # 第二步，重新建堆
        jian_dui(heap)
    print(result)


import random

heap = list(range(10))
random.shuffle(heap)
print(heap)
# heap = [8, 5, 7, 9, 2, 10, 1, 4, 6, 3, 1]
heap_sort(heap)
