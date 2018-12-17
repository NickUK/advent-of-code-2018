# Day 17 part 1+2
 
from collections import defaultdict
import sys

sys.setrecursionlimit(3000)

DIR_LEFT = (-1, 0)
DIR_RIGHT = (1, 0)
DIR_DOWN = (0, 1)


def parse_clay(file_name):
  res = defaultdict(bool)
  with open(file_name) as f:
    for line in f.readlines():
      xy = line[0]
      split_coords = line.split(", ")
      first = int(split_coords[0][2:])

      p2 = split_coords[1].strip()[2:].split("..")
      for second in range(int(p2[0]), int(p2[1]) + 1):
        if xy == "x":
          res[(first, second)] = True
        else:
          res[(second, first)] = True

  return res


def solve(xy, dir):
  flowing.add(xy)

  down = (xy[0], xy[1] + 1)

  if not clay[down]:
    if down not in flowing and down[1] >= 0 and down[1] <= max_y:
      solve(down, DIR_DOWN)
    if down not in settled:
      return False

  left = (xy[0] - 1, xy[1])
  right = (xy[0] + 1, xy[1])

  left_filled = clay[left] or (left not in flowing and solve(left, dir=DIR_LEFT))
  right_filled = clay[right] or (right not in flowing and solve(right, dir=DIR_RIGHT))

  if dir == DIR_DOWN and left_filled and right_filled:
    settled.add(xy)

    while left in flowing:
      settled.add(left)
      left = (left[0] - 1, left[1])

    while right in flowing:
      settled.add(right)
      right = (right[0] + 1, right[1])

  return dir == DIR_LEFT and (left_filled or clay[left]) or dir == DIR_RIGHT and (right_filled or clay[right])


clay = parse_clay("input")
#clay = parse_clay("testinput2")
settled = set()
flowing = set()
water = (500, 0)

clay_ys = list(map(lambda c: c[1], clay))
min_y, max_y = min(clay_ys), max(clay_ys)

solve(water, DIR_DOWN)

print(len([x for x in (flowing | settled) if min_y <= x[1] <= max_y])) # Part 1
print(len([x for x in settled if min_y <= x[1] <= max_y])) # Part 2
