# part 1
def pt1(f):
    l, r = [], []
    for x in open(f):
        a, b = map(int, x.split())
        l.append(a)
        r.append(b)
    return sum(abs(a - b) for a, b in zip(sorted(l), sorted(r)))

print(pt1('1.txt'))

# part 2
def pt2(f):
    l, r = [], []
    for x in open(f):
        a, b = map(int, x.split())
        l.append(a)
        r.append(b)
    return sum(n * r.count(n) for n in l)

print(pt2('1.txt'))