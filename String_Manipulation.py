a = 6
b = 1
c = 2

result = []

max_seq = 6+1+2

for x in range(max_seq):
    if a > b and a > c:
        result.append('a')
        a = a - 1
    if b > a and b > c:
        result.append('b')
        b = b - 1
    if c > a and c > b:
        result.append('c')
        c = c - 1

print(result)
