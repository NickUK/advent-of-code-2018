# Day 18 part 1+2

import collections


def parse(test_file):
  ground = set()
  trees = set()
  lumber = set()
  max_x = 0
  max_y = 0
  with open(test_file) as f:
    for y, line in enumerate(f.readlines()):
      line = line.strip()
      max_y = max(max_y, y)
      for x, char in enumerate(line):
        max_x = max(max_x, x)
        if char == ".":
          ground.add((x, y))
        elif char == "#":
          lumber.add((x, y))
        else:
          trees.add((x, y))

  return ground, trees, lumber, (max_x, max_y)


def adjacent(p):
  return [(p[0]-1, p[1]), (p[0]+1, p[1]),
          (p[0], p[1]-1), (p[0]+1, p[1]-1), (p[0]-1, p[1]-1),
          (p[0], p[1]+1), (p[0]+1, p[1]+1), (p[0]-1, p[1]+1)]


def minute(ground, trees, lumber, max_xy):
  new_ground = set()
  new_trees = set()
  new_lumber = set()
  
  for x in range(max_xy[0]+1):
    for y in range(max_xy[1]+1):
      point = (x, y)
      surrounding = adjacent(point)
      
      if point in ground:
        if len([x for x in trees if x in surrounding]) >= 3:
          new_trees.add(point)
        else:
          new_ground.add(point)
        
      elif point in trees:
        if len([x for x in lumber if x in surrounding]) >= 3:
          new_lumber.add(point)
        else:
          new_trees.add(point)
          
      else:
        if len([x for x in lumber if x in surrounding]) >= 1 and len([x for x in trees if x in surrounding]) >= 1:
          new_lumber.add(point)
        else:
          new_ground.add(point)
  
  return new_ground, new_trees, new_lumber


def print_yard(ground, trees, _, max_xy, min):
  print("\nYard at minute:", min, "\n")
  for y in range(max_xy[1]+1):
    line = ""
    for x in range(max_xy[0]+1):
      point = (x, y)
      if point in ground:
        line = line + "."
      elif point in trees:
        line = line + "|"
      else:
        line =  line + "#"

    print(line, flush=True)
  #input()


def play(g, t, l, max_xy, max_rounds, do_print):
  if do_print:
    print_yard(g, t, l, max_xy, "initial")

  last_value = 0
  diffs = []
  for i in range(1, max_rounds+1):
    g, t, l = minute(g, t, l, max_xy)
    if do_print:
      print_yard(g, t, l, max_xy, i)

    new_value = len(t) * len(l)
    print("Round:", i, "Value:", new_value, new_value - last_value)
    diffs.append((new_value, new_value-last_value))
    last_value = new_value

    # Look for a pattern
    duplicates = [item for item, count in collections.Counter(diffs).items() if count > 1]
    if len(duplicates) > 0:
      duplicate = duplicates[0]
      index = diffs.index(duplicate)
      pattern_len = (diffs[index+1:].index(duplicate) + index + 1) - index
      print("Pattern len:", pattern_len, "start of pattern:", duplicate, "on round:", i)

      # Find out how many more steps we would have at our target rounds..
      more_steps = ((max_rounds - i) % pattern_len)
      start = duplicate[0]

      # Apply the last steps
      for step in diffs[index+1:index+1+more_steps]:
        start += step[1]

      print("Part 2:", start)
      return


  print("Wooded areas:", len(t))
  print("Lumberyards:", len(l))
  print("Total value:", len(t) * len(l))


ground, trees, lumber, max_xy = parse("input")
print("Area size:", max_xy)
play(ground, trees, lumber, max_xy, 10, False) # Part 1
play(ground, trees, lumber, max_xy, 1000000000, False) # Part 2


