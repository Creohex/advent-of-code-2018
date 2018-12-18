import re

def part_one():
    counts = [0, 0]
    for word in open('input.txt'):
        dict = {}
        for c in word:
            dict[c] = 1 if c not in dict else dict[c] + 1
        has = [False, False]
        for _, e in dict.items():
            if e==2:
                has[0] = True
            if e==3:
                has[1] = True
        if has[0]:
            counts[0] += 1
        if has[1]:
            counts[1] += 1
    return counts[0] * counts[1]

def part_two():
    arr = []
    for w in open('input.txt'):
        arr.append(w.strip())

    for i in range(len(arr)):
        word = arr[i]
        for w in arr:
            different = 0
            for j in range(len(word)):
                if word[j] != w[j]:
                    different += 1
                if different >= 2:
                    break
            if different == 1:
                res = ""
                for e in range(len(w)):
                    res += word[e] if word[e] == w[e] else ''
                return res

print(part_one())
print(part_two())


