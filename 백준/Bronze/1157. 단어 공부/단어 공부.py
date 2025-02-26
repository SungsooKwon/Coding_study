from collections import Counter

word = input().upper()

counter = Counter(word)

max_count = max(counter.values())
most_common = []
for k, v in counter.items():
    if v == max_count:
        most_common.append(k)

if len(most_common) > 1:
    print("?")
else:
    print(most_common[0])
