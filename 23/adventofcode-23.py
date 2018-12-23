# Day 23 part 1+2

from z3 import *


def parse(file_name):
  nanobots = []
  with open(file_name) as f:
    for line in f.readlines():
      pos = list(map(lambda x: int(x), line[line.index("<")+1:line.rfind(">")].split(",")))
      radius = int(line.strip().split(", r=")[1])
      nanobots.append((pos, radius))
  return nanobots


def manhatten(xyz_a, xyz_b):
  return abs(xyz_b[0] - xyz_a[0]) + abs(xyz_b[1] - xyz_a[1]) + abs(xyz_b[2] - xyz_a[2])


def part1(nanobots):
  sorted_strongest = sorted(nanobots, key=lambda p: (p[1]), reverse=True)
  strongest = sorted_strongest[0]
  
  in_range = 0
  for other in sorted_strongest:
    if manhatten(strongest[0], other[0]) <= strongest[1]:
      in_range += 1
  
  print(in_range)


def z3_abs(x):
  return If(x >= 0, x, -x)


def z3_manhatten(x, y):
  return z3_abs(x[0] - y[0]) + z3_abs(x[1] - y[1]) + z3_abs(x[2] - y[2])


def part2(nanobots):
  x = Int('x')
  y = Int('y')
  z = Int('z')
  orig = (x, y, z)

  cost_expr = 0
  for bot in nanobots:
    cost_expr += If(z3_manhatten(orig, bot[0]) <= bot[1], 1, 0)

  opt = Optimize()
  opt.maximize(cost_expr)
  opt.minimize(z3_manhatten((0,0,0), orig))
  opt.check()
  model = opt.model()
  print(manhatten((0,0,0), (model[x].as_long(), model[y].as_long(), model[z].as_long())))
  

bots = parse("input")
part1(bots) # Part 1
part2(bots) # Part 2