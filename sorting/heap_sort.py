#!/usr/bin/env python
# coding=utf-8

def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    print lists
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
        print lists


def build_heap(lists, size):
    for i in range(0, (size/2))[::-1]:
        adjust_heap(lists, i, size)

def adjust_heap(lists, i, size):
    lchild = 2*i + 1
    rchild = 2*i + 2
    max = i
    if i<size/2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]

            adjust_heap(lists, max, size)
            
a = [4, 5, 1, 3, 6, 2, 8, 9, 7, 0]

heap_sort(a)

print a


