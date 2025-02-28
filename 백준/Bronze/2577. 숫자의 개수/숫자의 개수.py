a = int(input())
b = int(input())
c = int(input())

total = a * b * c

from collections import Counter

total_str = str(total)
count_dict = Counter(total_str)

freq_list = [count_dict.get(str(i), 0) for i in range(0, 10)]

for freq in freq_list:
    print(freq)

