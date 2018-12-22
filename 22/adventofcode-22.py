# Day 22 part 1+2

import heapq

cave_erosions = {}


def erosion_level(pos, target, depth):
  global cave_erosions

  if pos in cave_erosions:
    return cave_erosions[pos]

  res = ((geologic_index(pos, target, depth) + depth) % 20183)
  cave_erosions[pos] = res
  return res


def risk(erosion_level):
  return erosion_level % 3


def geologic_index(pos, target, depth):
  if pos == (0, 0) or pos == target:
    return 0
  
  if pos[1] == 0:
    return pos[0] * 16807
  elif pos[0] == 0:
    return pos[1] * 48271
  else:
    return erosion_level((pos[0]-1, pos[1]), target, depth) * erosion_level((pos[0], pos[1]-1), target, depth)


def print_cave(cave, target):
  for y in range(target[1]+1):
    line = ""
    for x in range(target[0]+1):
      val = cave[(x, y)]

      if (x, y) == (0, 0):
        line = line + "M"
      elif (x, y) == target:
        line = line + "T"
      elif val == 0:
        line = line + "."
      elif val == 1:
        line = line + "="
      else:
        line = line + "|"

    print(line)


def plot_cave(depth, target, extra=0):
  cave = {}

  for y in range(target[1]+1+extra):
    for x in range(target[0]+1+extra):
      test_pos = (x, y)
      cave[test_pos] = risk(erosion_level(test_pos, target, depth))
  
  #print_cave(cave, target)
  
  if extra == 0:
    print(sum(cave.values()), flush=True)


def adjacent(xy):
  return [(xy[0]-1,xy[1]), (xy[0]+1,xy[1]), (xy[0],xy[1]-1), (xy[0],xy[1]+1)]


def find_target(target):
  global cave_erosions

  item = 1 # 0 - Neither, 1 - Light, 2 - Climbing gear
  queue = [(0, 0, 0, item)]
  best_options = {} 
  
  target_set = (target[0], target[1], 1)
  while len(queue) > 0:
      minutes, x, y, item = heapq.heappop(queue)
      
      if (x, y, item) in best_options and best_options[(x, y, item)] <= minutes:
        continue
      best_options[(x, y, item)] = minutes

      if (x, y, item) == target_set:
        return minutes
      
      for i in range(3):
          if i != item and i != risk(cave_erosions[(x, y)]):
              heapq.heappush(queue, (minutes + 7, x, y, i))
      
      for option in adjacent((x, y)):
          if option in cave_erosions and item != risk(cave_erosions[option]): # Item numbers line up with terrain they can't be used on
              heapq.heappush(queue, (minutes + 1, option[0], option[1], item))
              

depth = 11820
target = (7, 782)

plot_cave(depth, target) # Part 1
plot_cave(depth, target, 1000) # (expand the cave size for part 2)
print(find_target(target)) # part 2