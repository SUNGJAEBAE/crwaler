arr = ['asdf', 'dddd', 'portal']


def findi(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i+1

    return -1
