#!/usr/bin/env python
from math import log

def normalize2int(inputs, bins, zeroindexed=True):
    assert inputs, "Need some inputs, list of numbers"
    assert isinstance(bins, int), "Need int for bins"

    minx = min(inputs)
    maxx = max(inputs)
    step = int(round((maxx - minx) / float(bins)))
    print "[DEBUG] step= {:d} bins= {:d}".format(step,bins)
    retval = [ int(round((i - minx) / step)) for i in inputs ]

    if not zeroindexed:
        retval = [ i+1 for i in retval ]

    ### n,_ = np.histogram(data,bins=bins)
    ### n2=n*(len(numofbars)-1)/(max(n))
    print "[DEBUG] {}".format(inputs)
    return retval


def normalize2intlog(inputs, bins, zeroindexed=True):
    assert inputs, "Need some inputs, list of numbers"
    assert isinstance(bins, int), "Need int for bins"

    minx = log( min(inputs))
    maxx = log( max(inputs))
    step = int(round((maxx - minx) / float(bins)))
    assert step>0, "Step needs to be positive"
    print "[DEBUG] step= {:d} bins= {:d}".format(step,bins)
    retval = [ int(round((log(i) - log(minx)) / step)) for i in inputs ]

    if not zeroindexed:
        retval = [ i+1 for i in retval ]

    ### n,_ = np.histogram(data,bins=bins)
    ### n2=n*(len(numofbars)-1)/(max(n))
    print "[DEBUG] {}".format(inputs)
    return retval

if __name__ == '__main__':
    print '====='
    print normalize2int([0,1,2,3,4],5)
    print '====='
    print normalize2int(range(0,11),10)
    print '====='
    print normalize2int([1,2,3,4,5],5)
    print '====='
    print normalize2int([10,5,2,40,19],5)
    print '====='
    print normalize2int([10,5,20,40,31],10)
    print '====='
    print normalize2int([0,1,2,3,4], 5, zeroindexed=False)
    print '====='
    print normalize2int(range(0,11), 10, zeroindexed=False)
    print '====='
    print normalize2int(range(1,21,2), 10, zeroindexed=False)
    print '====='
    print normalize2int(range(1,21,2), 7, zeroindexed=False)
    print '====='
    print '====='
    print normalize2intlog(range(1,6,1), 5, zeroindexed=False)
