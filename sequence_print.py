# Print all the possible 'a','b','c' combination in such a way that, any alphabet does not repeat more than 2 times.
# for example if string has '5 'a'', '2'b'', '2'c'' then it can print aabbccaa or aabbaccaa or aaccaabba

from itertools import permutations
import math
import re

a = int(input())
b = int(input())
c = int(input())
num = math.ceil((a + b + c) / 2)

str_val = a*'a'+b*'b'+c*'c'
str_per = list(set(list(permutations(str_val))))
temp_str, output_str = [], []
val = ["".join(i) for i in str_per]
for each in val:
    all_find_str = re.findall(r"([a-z])\1{2,}", each)
    if not all_find_str:
        output_str.append(each)
    else:
        all_find_str = re.findall(r"([a-z])\1{2,}", each[:num])
        if not all_find_str:
            temp_str.append(each[:num])
if output_str:
    print("Output is:", set(output_str))
else:
    print("Output is:", set(temp_str))
