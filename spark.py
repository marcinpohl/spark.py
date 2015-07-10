# -*- coding: utf-8 -*-

"""
spark.py
~~~~~~~~

A port of @holman's spark project for Python.
"""

import sys

sparks = u' ▁▂▃▄▅▆▇█'

def spark_string(ints, fit_min=False):
    """Returns a spark string from given iterable of ints.

    Keyword Arguments:
    fit_min: Matches the range of the sparkline to the input integers
             rather than the default of zero. Useful for large numbers with
             relatively small differences between the positions
    """
    min_range = 0
    if fit_min:
        min_range = min(ints)
    try:
        sparks = [ int(i) for i in ints ]
    except TypeError as err:
        print err

    step_range = max(ints) - min_range
    step = ((step_range) / float(len(sparks) - 1)) or 1
    return u''.join(sparks[int(round((i - min_range) / step))] for i in ints)

def logspark_string(ints, fit_min=False):
    """Returns a spark string from given iterable of ints.

    Keyword Arguments:
    fit_min: Matches the range of the sparkline to the input integers
             rather than the default of zero. Useful for large numbers with
             relatively small differences between the positions
    """
    min_range = 0.0000000001
    if fit_min:
        min_range = min(ints)

    mininput=1/log(min(ints))
    try:
        sparks = [ log(i)*mininput for i in ints ]
    except TypeError as err:
        print err

    step_range = max(ints) - min_range
    step = ((step_range) / float(len(sparks) - 1)) or 1
    return u''.join(sparks[int(round((i - min_range) / step))] for i in ints)


def spark_print(ints, stream=None, fit_min=False):
    """Prints spark to given stream."""
    if stream is None:
        stream = sys.stdout
    stream.write(spark_string(ints, fit_min=fit_min).encode('utf-8'))


def usage():
    print "spark\n"
    print "USAGE:"
    print "  spark.py [spaces separated values]\n"
    print "EXAMPLES:"
    print "  spark.py 1 5 22 13 53"
    spark_print([1, 5, 22, 13, 53])
    print
    print "  spark.py 0 30 55 80 33 150"
    spark_print([0, 30, 55, 80, 33, 150])
    print
    print
    print "  spark.py 1 2 3 5 7 11 13 19 23 29"
    spark_print([1.0, 2, 3, 5, 7, 11, 13, 19, 23, 29])

if __name__ == '__main__':
    if len(sys.argv) > 1:
        ### sparks = map(int, sys.argv[1:])
        sparks = [ int(i) for i in sys.argv[1:] ]
        spark_print(sparks)
        print
    else:
        usage()
