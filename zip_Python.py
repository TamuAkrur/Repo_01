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

# Cut the elements of the highest and end

# array of entries
entries = [num1, num2, num3]

# highest in the entry
high = max(entries)

a_counter = 0
b_counter = 0
c_counter = 0
reps = 2

while True :
    # take elements from highest, and reduce it
    # condition to find most elements
    if len(a) >= len(b) and len(a) >= len(c):
        # action for a
        result.append(a[0])
        del a[0]
        a_counter = a_counter + 1

    if len(b) >= len(a) and len(b) >= len(c):
        # action for b
        result.append(b[0])
        del b[0]
        b_counter = b_counter + 1

    if len(c) >= len(b) and len(c) >= len(a):
        # action for a
        result.append(b[0])
        del b[0]
        c_counter = c_counter + 1
    print('Hello')

