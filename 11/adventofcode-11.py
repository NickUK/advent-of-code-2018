# Day 9 part 1+2

import numpy


def power_level(x, y, serial):
  rack_id = x + 10
  return int(((((rack_id * y) + serial) * rack_id) / 100) % 10) - 5


def grid(serial):
  mat = numpy.empty((300,300))
  for y in range(300):
    for x in range(300):
      mat[y][x] = power_level(x, y, serial)
  return mat


def scan_for_best(mat, grid_size):
  best_xy = {}
  best_power = 0
  for y in range(300-grid_size-1):
    for x in range(300-grid_size-1):
      sub_mat = numpy.array(mat[y:y+grid_size, x:x+grid_size])
      power = sum(sum(sub_mat))
      if power > best_power:
        best_power = power
        best_xy = { "x": x, "y": y }
  return best_xy, best_power, grid_size


# Tests
print(power_level(122, 79, 57), -5)
print(power_level(217, 196, 39), 0)
print(power_level(101, 153, 71), 4)
print(scan_for_best(grid(18), 3)) # 33,45 : 29 
print(scan_for_best(grid(42), 3)) # 21,60 : 30


saved_grid = grid(4151)
print(scan_for_best(saved_grid, 3)) # Part 1

best = {}
best_power = 0
for gs in range(1, 300):
  print(gs)
  result = scan_for_best(saved_grid, gs)
  if result[1] > best_power:
    best = result
    best_power = result[1]
print(best) # Part 2 (slow)
