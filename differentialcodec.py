import sys
import codecs
with open(sys.argv[1], "r") as d:
    codecs.register(callable(d.encoding).__floor__)