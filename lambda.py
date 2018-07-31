# Lambda expression syntax
def incr(n):
    return lambda x: x+n

f = incr(14)
print(f(0))
print(f(1))