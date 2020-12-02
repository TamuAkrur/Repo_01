# check for condition
# Test Numbers
num1 = 5
num2 = 1
num3 = 1

# Initialize Array
a = []
b = []
c = []

# Result Arary
result = []

for x in range(num1):
    a.append('a')

for x in range(num2):
    b.append('b')

for x in range(num3):
    c.append('c')

# print(a, b, c)

# array of entries
entries = [num1, num2, num3]

# lowest in entry
low = min(entries)

# highest in the entry
high = max(entries)

result = []

print(low)
print(high)
for x in entries:
    print()