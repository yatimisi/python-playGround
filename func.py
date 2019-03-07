def add(n1, n2=None):
    if n2 is None:
        n2 = n1
        
    return n1 + n2

print(add(1))
print(add(1, 2))