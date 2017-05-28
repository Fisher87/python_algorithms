#!/usr/bin/env python
# coding=utf-8

"""

author:(Fisher:992049896@qq.com)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Quick Sort Instruction:

"""

#TODO(@Fisher)    Date:2017-05-28
class QuickSort(object):
    def sort(self, data):
        if data is None:
            raise TypeError()

        if len(data) < 2:
            return data

        equal = []
        left = []
        right = []
        pivot_index = len(data)/2
        pivot_value = data[pivot_index]
        for item in data:
            if item == pivot_value:
                equal.append(item)
            elif item < pivot_value:
                left.append(item)
            else:
                right.append(item)

        left_ = self.sort(left)
        right_ = self.sort(right)
        return left_ + equal + right_


quick_sort = QuickSort()
sorted_ = quick_sort.sort([3,1,5,7,2,4,9,6])
print sorted_
