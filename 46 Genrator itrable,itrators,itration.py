"""
itrable --> __iter__() or __getitem__()
when we run this it produce itratore
itrators --> __next__() which gives next items
and this prodeuce iteration
 for most see also register -->2
"""

def gen(n):
    for i in range(n):
        yield i
a=gen(3)
print(a) # it will tell it is genrator
print(a.__next__()) # it will print next about it
print(a.__next__())
print(a.__next__())
 # print(a.__next__()) # this will give error beacuse itration has stopped it is
 # only at 3

