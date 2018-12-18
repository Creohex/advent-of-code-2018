import re


def part_one():
    arr = [[0 for j in range(1000)] for i in range(1000)]
    over_claimed = 0
    for claim in open('input.txt'):
        id, left, top, width, height = re.findall("\d+", claim)
        left, top, width, height = int(left), int(top), int(width), int(height)
        for i in range(top, top + height):
            for j in range(left, left + width):
                arr[i][j] += 1
                if arr[i][j] == 2:
                    over_claimed += 1
    return over_claimed

def part_two():
    arr = [[0 for j in range(1000)] for i in range(1000)]
    for claim in open('input.txt'):
        id, left, top, width, height = re.findall("\d+", claim)
        left, top, width, height = int(left), int(top), int(width), int(height)
        for i in range(top, top + height):
            for j in range(left, left + width):
                arr[i][j] += 1
    for claim in open('input.txt'):
        id, left, top, width, height = re.findall("\d+", claim)
        left, top, width, height = int(left), int(top), int(width), int(height)

        overlaps = False
        for i in range(top, top + height):
            if overlaps:
                break
            for j in range(left, left + width):
                if overlaps:
                    break
                if arr[i][j] > 1:
                    overlaps = True
        if not overlaps:
            return id


print(part_one())
print(part_two())
