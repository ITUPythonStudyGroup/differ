import copy

__all__ = ['merge', 'delta']

# remove all of b in a
def removeBinA(a,b, removeOnDiffValues = True):
    for key in b.keys():
        if key in a:
            if type(a[key]) is dict:
                removeBinA(a[key], b[key], removeOnDiffValues)
                if not a[key]: # if the dictionary is empty
                    a.pop(key, None)
            elif a[key] == b[key] or removeOnDiffValues:
                a.pop(key, None)


def setBinA(a,b):
    for key in b.keys():
        if key in a and type(a[key]) is dict:
            setBinA(a[key], b[key])
        else:
            a[key] = b[key]

def merge(a,delta):
    acopy = copy.deepcopy(a)
    setBinA(acopy, delta['set'])
    removeBinA(acopy, delta['delete'])
    return acopy

def delta(a,b):
    delta = {}
    bcopy = copy.deepcopy(b)
    acopy = copy.deepcopy(a)

    removeBinA(bcopy, a, False)
    delta['set'] = bcopy

    removeBinA(acopy,b)
    delta['delete'] = acopy
    return delta
