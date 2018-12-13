# Day 12 part 1+2

from collections import defaultdict
from functools import reduce


def parse_rules(file_name):
  with open(file_name) as f:
    return tuple(
      map(lambda ruley: ruley["from"],
          (filter(lambda rule: rule["to"] == "#",
          map(lambda x: {"from": x.split(' ')[0],"to": x.split(' ')[2].strip()},
              f.readlines()))))
    )


def mutate(line, rules):
  # Pad right
  line = line + ('.' * max(4 - (len(line) - line.rfind("#")), 0))

  # Pad left
  first_plant = line.find("#")
  if first_plant < 3:
    line = ('.' * (3- first_plant)) + line

  return ".." + reduce(lambda x, y: str(x) + str(y), map(lambda x: "#" if line[x-2:x+3] in rules else '.', range(2, len(line)-2))) + "..", max(3-first_plant, 0)


def sum_plants(input_str, total_left):
  return reduce(lambda x, y: x + y, map(lambda x: x - total_left if input_str[x] == "#" else 0, range(len(input_str))))


def process(input, rules, iters):
  left = 0

  prev_score = sum_plants(input, left)
  last_diff = 0

  for n in range(min(1000, iters)):
    input, more_left = mutate(input, rules)
    left = left + more_left

    score = sum_plants(input, left)
    last_diff = score - prev_score
    prev_score = score

  if iters > 1000:
    return last_diff * (iters - 1000) + sum_plants(input, left)
  
  return prev_score


print(process("#..#.#..##......###...###", parse_rules("testinput"), 20)) # Part 1
print(process("#.##.##.##.##.......###..####..#....#...#.##...##.#.####...#..##..###...##.#..#.##.#.#.#.#..####..#" + ".....", parse_rules("input"), 50000000000)) # Part 2