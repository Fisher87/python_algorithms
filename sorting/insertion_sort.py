#!/usr/bin/env python
# coding=utf-8

"""

author:(Fisher@992049896@qq.com)
~~~~~~~~~~~~~~~~~~~
Straight Insertion Sort Introduct:
    ...

complexity:
    Time:
    Space:

"""
#TODO(@Fisher) Date:2017-05-27

class InsertionSort(object):
    def sort(self, data):
        if data is None:
            raise TypeError()

        if len(data) < 2:
            return data

        length = len(data)
        for index in xrange(1, length):
            tmp = data[index]
            for i in xrange(index, 0, -1):
                if data[i-1]>tmp:
                    data[i-1], data[i] = data[i], data[i-1]
                    print data
        return data


insert_sort = InsertionSort()

sorted_ = insert_sort.sort([3,1,5,7,2,4,9,6])
print sorted_

#Refer from github(http://nbviewer.jupyter.org/github/donnemartin/interactive-coding-challenges/blob/master/sorting_searching/insertion_sort/insertion_sort_solution.ipynb)
class InsertionSort_(object):
    def sort(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if len(data) < 2:
            return data
        for r in range(1, len(data)):
            for l in range(r):
                if data[r] < data[l]:
                    temp = data[r]
                    data[l+1:r+1] = data[l:r]
                    data[l] = temp
            print data

        return data

insert_sort = InsertionSort_()

sorted_ = insert_sort.sort([3,1,5,7,2,4,9,6])
print sorted_
