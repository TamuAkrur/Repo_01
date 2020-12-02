def print_num():
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

    # max possible connection
    max_connection = len(a) + len(b) + len(c)
    # print(max_connection)

    # max repetition is 2
    reps = 2

    # loop until maximum possible chain
    # Where num1+num2+num3 < 0 is all numbers are below 100

    for x in range(max_connection):

        # check len of a is not 0, then break
        if len(a) != 0:
            for y in range(reps):
                # Add twice if length is greater than 2
                if len(a) > 1:
                    # check other array before adding to result set
                    if len(b) > 1 and len(c) > 1:
                        result.append(a[y])
                        # remove from parent array
                        del a[y]
                        if len(a) == 1:
                            print('1 value remains from A')
                        # # move to result array
                        # result.append(a[0])
                        # # remove from parent array
                        # del a[0]
        else:
            continue

        if len(b) != 0:
            for z in range(reps):
                if len(b) > 1:
                    if len(a) > 1 and len(c) > 1:
                        result.append(b[z])
                        del b[z]
                        if len(b) == 1:
                            print('1 value remains from B')

        else:
            continue

        if len(c) != 0:
            for n in range(reps):
                if len(c) > 1:
                    if len(a) > 1 and len(c)>1:
                        result.append(c[n])
                        del c[n]
                        if len(c) == 1:
                            print('1 value remains from C')
        else:
            continue

    print(*result, sep='')
    print(a)
    print(b)
    print(c)


print_num()
