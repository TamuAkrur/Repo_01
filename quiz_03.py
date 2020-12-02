import random

a = []
b = []
c = []

result = []

num1 = 1
num2 = 1
num3 = 6

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


# max possible connection
max_connection = len(a) + len(b) + len(c)
# print(max_connection)

# max repetition is 2
reps = 2

single_letters = []

remaining_letters = []

# loop until maximum possible chain
for x in range(max_connection):

    if len(a) >= 2:
        for aa in range(reps):
            # Append only if array is bigger than 2, if there is no remainig c and b, push it to another list
            if len(a) != 0 and len(c) != 0:
                result.append(a[0])
                # remove from parent array
                del a[0]
            else:
                remaining_letters.append(a[0])
                # remove from parent array
                del a[0]
    else:
        # if len(a) == 0:
        #     continue
        if len(a) == 1:
            single_letters.append(a[0])
            del a[0]

    if len(b) >= 2:
        for bb in range(reps):
            if len(b) != 0 and len(c) != 0:
                result.append(b[0])
                del b[0]
            else:
                remaining_letters.append(b[0])
                # remove from parent array
                del b[0]
    else:
        # if len(b) == 0:
        #     continue
        if len(b) == 1:
            single_letters.append(b[0])
            del b[0]

    if len(c) >= 2:
        if len(a) != 0 and len(b) != 0:
            for cc in range(reps):
                result.append(c[0])
                del c[0]
            else:
                remaining_letters.append(c[0])
                # remove from parent array
                del c[0]
    else:
        # if len(c) == 0:
        #     continue
        if len(c) == 1:
            single_letters.append(c[0])
            del c[0]
# join two result set and single letters
# only if last letter and first letter of result set and single letters set is not same


print(*result, sep=' ')
print(a)
print(b)
print(c)
print(single_letters)
print(remaining_letters)
# first_letter = single_letters[0]
# last_letter = result[-1]
# print(first_letter, last_letter)
#
# if first_letter != last_letter:
#     final_res = result + single_letters
#     print(*final_res, sep=' ')
# else:
#     random.shuffle(single_letters)
