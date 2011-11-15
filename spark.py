# -*- coding: utf-8 -*-

"""
spark.py
~~~~~~~~

A port of @holman's spark project for Python.
"""

import sys

ticks = (u'▁', u'▂', u'▃', u'▅', u'▆', u'▇')


def spark_string(ints):
    """Returns a spark string from given iterable of ints."""
    step = ((max(ints) - min(ints)) / (len(ticks) - 1))
    return u' '.join([ticks[(i/step)] for i in ints])


def spark_print(ints, stream=None):
    """Prints spark to given stream."""
    if stream is None:
        stream = sys.stdout

    stream.write(spark_string(ints))
