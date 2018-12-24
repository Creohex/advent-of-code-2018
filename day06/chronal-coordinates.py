import collections, re


def read_input():
    return list(map(tuple, map(lambda _: (int(m[0]) for m in re.finditer(r"\d+", _)), open('input.txt'))))

def get_bounds(coords):
    """ returns: (left, right, top, bottom) """
    return min(x for x, y in coords), max(x for x, y in coords), min(y for x, y in coords), max(y for x, y in coords)

def build_coord_plane(coords):
    left, right, bottom, top = get_bounds(coords)
    plane = {}
    max_len = (top - bottom) + (right - left)
    for x in range(left, right + 1):
        for y in range(bottom, top + 1):
            closest_coords = []
            min_distance = int(max_len)
            for xx, yy in coords:
                distance = abs(x - xx) + abs(y - yy)
                if distance <= min_distance:
                    min_distance = distance
                    closest_coords.append((xx, yy, distance))
            closest_coords = [(xx, yy, distance) for xx, yy, distance in closest_coords if distance == min_distance]
            if len(closest_coords) == 1:
                plane[x, y] = (closest_coords[0][0], closest_coords[0][1])
            elif len(closest_coords) > 1:
                plane[x, y] = '.'
    return plane

def part_one():
    coords = read_input()
    plane = build_coord_plane(coords)

    # generate inf-area coords list
    exclude_coords = []
    borders = list(get_bounds(coords))
    for coords, owner in plane.items():
        if len(owner) == 2:
            x, y = coords
            cx = owner[0]
            cy = owner[1]
            if (x in borders[:2] or y in borders[2:]) and owner not in exclude_coords:
                exclude_coords.append(owner)

    # calculate coord areas, ignoring coords in inf-area list
    total_areas = {}
    for coord, owner in [(coords, owner) for (coords, owner) in plane.items() if len(owner) == 2 and owner not in exclude_coords]:
        (owner_x, owner_y) = owner
        if owner not in total_areas.keys():
            total_areas[owner_x, owner_y] = 1
        else:
            total_areas[owner_x, owner_y] = total_areas[owner] + 1

    # return max area
    return max(total_areas.values())


def part_two():
    coords = read_input()
    left, right, bottom, top = get_bounds(coords)
    region_size = 0

    for x in range(left, right + 1):
        for y in range(bottom, top + 1):
            distance = 0
            for cx, cy in coords:
                distance += abs(cx - x) + abs(cy - y)
            if distance < 10000:
                region_size += 1

    return region_size


print(part_one())
print(part_two())
