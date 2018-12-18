

def part_one():
    res = 0
    for line in open('input.txt', 'r'):
        res = res - int(line[1:]) if line[0] is '-' else res + int(line[1:])
    return res

def part_two():
    res = 0
    arr = [0]
    while True:
        for line in open('input.txt', 'r'):
            res = res - int(line[1:]) if line[0] is '-' else res + int(line[1:])
            if res in arr:
                return res
            else:
                arr.append(res)

print(part_one())
print(part_two())
