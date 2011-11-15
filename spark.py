# -*- coding: utf-8 -*-

import sys

ticks = (u'▁', u'▂', u'▃', u'▅', u'▆', u'▇')

def spark_string(ints):
    """Returns a spark string from given iterable of ints."""
    step = ((max(ints) - min(ints)) / (len(ticks) - 1))

    s = []
    for i in ints:
        s.append(ticks[(i/step)])
        s.append(' ')

    return u''.join(s)


def spark_print(ints, stream=None):
    """Prints spark to given stream."""

    if stream is None:
        stream = sys.stdout

    stream.write(spark_string(ints))
