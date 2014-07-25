from random import randint
from collections import defaultdict
from itertools import groupby
from timeit import Timer
from sys import argv
from operator import eq

narrow = [randint(1,2) for x in xrange(1000)]
wide = [randint(1,1000) for x in xrange(1000)]
vwide = [randint(1,10**10) for x in xrange(1000)]

def dictget(a):
    d = {}
    for v in a: d[v] = d.get(v, 0) + 1
    return d

def defaultd(a):
    d = defaultdict(int)
    for v in a: d[v] += 1
    return d

def itertool(a):
  return dict([(x,len(list(y))) for x,y in groupby(sorted(a))])

def makeset(a):
    d = {}
    for i in set(a):
        d[i] = a.count(i)
    return d

def ternary(a):
    d = {}
    for v in a: d[v] = d[v]+1 if v in d else 1
    return d

def fp(a):
    return dict(zip(set(a), map(a.count, set(a))))

def generator(a):
    return dict((i,a.count(i)) for i in set(a))

if __name__ == "__main__":
    fns = [dictget, defaultd, itertool, makeset, ternary, fp, generator]
    tests = [narrow, wide, vwide]
    for t in tests:
        for a in (f(t) for f in fns):
            for b in (f(t) for f in fns):
                if a != b:
                    raise "%s != %s" % (a, b)

    print "      test\tnarrow\twide\tvwide"
    for timed in fns:
        timed = timed.__name__
        ntests = 500
        n = Timer('%s(narrow)' % timed, 'from __main__ import narrow, %s' % timed).timeit(ntests)
        w = Timer('%s(wide)' % timed, 'from __main__ import wide, %s' % timed).timeit(ntests)
        v = Timer('%s(vwide)' % timed, 'from __main__ import vwide, %s' % timed).timeit(ntests)
        print "%10s\t%.3f\t%.3f\t%.3f" % (timed, n, w, v)
