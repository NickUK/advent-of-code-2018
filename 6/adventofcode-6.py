# Day 6 part 1+2

import numpy


def manhatten_dist(x1, y1, x2, y2):
  return abs(x2-x1) + abs(y2-y1)


points = []
with open("input") as f:
  for line in f.readlines():
    stripped = line.strip().split(",")
    points.append({"x":int(stripped[0]),"y":int(stripped[1])})

max_x = max(p['x'] for p in points)+1
max_y = max(p['y'] for p in points)+1
min_x = min(p["x"] for p in points)
min_y = min(p["y"] for p in points)

results = numpy.zeros((len(points)))
under_ten_k = 0
infs = []

for x in range(min_x, max_x):
  for y in range(min_y, max_y):
    dists = [manhatten_dist(x, y, p["x"], p["y"]) for p in points]
    min_dist = min(dists)

    if sum(dists) < 10000:
      under_ten_k = under_ten_k + 1

    if not dists.count(min_dist) > 1:
      results[dists.index(min_dist)] += 1

      # Keep track of the points extending into infinity
      if x == min_x or x == max_x or y == min_y or y == max_y:
        infs.append(dists.index(min_dist))

  
results = numpy.delete(results, infs)

print(max(results)) # Part 1
print(under_ten_k) # Part 2
