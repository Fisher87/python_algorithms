#!/usr/bin/env python
# coding=utf-8

class MergeSort(object):
    def sort(self, data):
        if data is None:
            raise TypeError()

        if len(data) < 2:
            return data
        partion = 2
        length = len(data)
        middle = length/2
        if middle>1:
            self.sort(data[0:middle])
            self.sort(data[middle+1:length])
        for i in xrange(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]

        return data


merge_sort = MergeSort()
sort_ = merge_sort.sort([3,1,5,7,2,4,9,6])
print sort_
