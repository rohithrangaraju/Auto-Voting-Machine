x = lambda a, b, *c : [a]+[b]+list(c)
print(x(5, 6, [2,3]))