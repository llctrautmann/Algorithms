'''
Description:

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
'''

def move_zeros(l):
    counter = 0
    while 0 in l:
        l.remove(0)
        counter += 1

    return l + [int(x) for x in counter * '0']
