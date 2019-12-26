"""
leetcode 239
Sliding Window Maximum
"""

"""
Time Complexity: O(N*logk)

Because python doesn't have an index_maxheap,so need to implement
Notes:
1)当“滑动窗口”要把左边界移除的时候,但是没有从一个堆中移除非最堆顶元素的操作;
2)找到即将要滑出边界的那个索引,索引值如何更新呢？新进来的那个数的索引,索引对 k 取模的那个索引进行更新.
"""

class IndexMaxHeap:
    def __init__(self, capacity):
        self.data = [None for _ in range(capacity)]
        self.indexes = [-1 for _ in range(capacity)]
        self.reverse = [-1 for _ in range(capacity)]
        self.count = 0
        self.capacity = capacity

    def size(self):
        return self.count

    def empty(self):
        return not self.count

    def insert(self, i, item):
        if self.count + 1 > self.capacity:
            raise Exception('heap is out of capacity')
        self.data[i] = item

        self.indexes[self.count] = i
        self.reverse[i] = self.count

        self.count += 1
        self.__shift_up(self.count - 1)

    def __shift_up(self, i):
        while i > 0 and self.data[self.indexes[i // 2]] < self.data[self.indexes[i]]:
            self.indexes[i // 2], self.indexes[i] = self.indexes[i], self.indexes[i // 2]

            self.reverse[self.indexes[i // 2]] = i // 2
            self.reverse[self.indexes[i]] = i

            i //= 2

    def __shift_down(self, i):
        while 2 * i <= self.count:
            idx = 2 * i
            # if idx + 1 <= self.count and self.data[self.indexes[idx]] > self.data[self.indexes[idx - 1]]:
            #     idx += 1
            if self.data[self.indexes[i]] >= self.data[self.indexes[idx]]:
                break
            self.indexes[i], self.indexes[idx] = self.indexes[idx], self.indexes[i]

            self.reverse[self.indexes[i]] = i
            self.reverse[self.indexes[idx]] = idx

            i = idx

    def pop(self):
        if self.count == 0:
            raise Exception('heap is null')
        ret = self.data[self.indexes[0]]
        self.indexes[0], self.indexes[self.count - 1] = self.indexes[self.count - 1], self.indexes[0]
        self.reverse[self.indexes[0]] = 0
        self.reverse[self.indexes[self.count - 1]] = self.count - 1

        self.reverse[self.indexes[self.count - 1]] = 0

        self.count -= 1
        self.__shift_down(1)
        return ret

    def pop_index(self):
        assert self.count > 0
        ret = self.indexes[0]
        self.indexes[0], self.indexes[self.count - 1] = self.indexes[self.count - 1], self.indexes[0]
        self.count -= 1
        self.__shift_down(0)
        return ret

    def peek(self):
        if self.count == 0:
            raise Exception('heap is null')
        return self.data[self.indexes[0]]

    def get_item(self, i):
        return self.data[i]

    def update(self, i, item):
        self.data[i] = item

        idx = self.reverse[i]
        self.__shift_down(idx)
        self.__shift_up(idx)

    def peek_index(self):
        if self.count == 0:
            raise Exception('heap is null')
        return self.indexes[0]


def max_sliding_window(nums, k):
    if not nums:
        return []

    index_maxheap = IndexMaxHeap(k)
    for i in range(k):
        index_maxheap.insert(i, nums[i])

    res = []
    for i in range(k, len(nums)):
        res.append(index_maxheap.peek())
        index_maxheap.update(i % k, nums[i])
    res.append(index_maxheap.peek())
    return res


"""
test sample
"""
if __name__=='__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    res = max_sliding_window(nums, k)
    print(res)
