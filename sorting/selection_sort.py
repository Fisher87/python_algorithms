#!/usr/bin/env python
# coding=utf-8

"""

author:(Fisher@992049896@qq.com)
~~~~~~~~~~~~~~~~~~~
选择排序介绍:
    step1:select the miniest number in list and exchange with data[0]
    setp2:select the second miniest number in other numbers and exchange
          with data[1]
    ...

complexity:
    Time:O(n^2)average, worst, best
    Space:O(1)iterative

"""
#TODO(@Fisher) Date:2017-05-26
class SelectionSort(object):
    def sort(self, data):
        if len(data) == 0:
            return 
        if len(data) < 2:
            return data

        length = len(data)
        for i in xrange(0, length-1):
            index = i
            min = data[i]
            for j in xrange(i, length):
                if data[j] < min:
                    min = data[j]
                    index = j
            data[i], data[index] = data[index], data[i]
        return  data


select = SelectionSort()
selected_data = select.sort([3,1,5,7,2,4,9,6])
print selected_data

#refer from github
class SelectionSorted(object):
    def sort(self, data):
        if data is None:
            raise TypeError('data cannot be none!')

        if len(data) < 2:
            return data

        for i in range(len(data)-1):
            min_index = i
            for j in range(i+1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
            if data[min_index] < data[i]:
                data[i], data[min_index] = data[min_index], data[i]

        return data
