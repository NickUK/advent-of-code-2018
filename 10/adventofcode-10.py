# Day 10 part 1+2
# python adventofcode-10.py > out.txt


import re
import numpy


def parse(file_name):
  with open(file_name) as f:
    results = []
    for line in f.readlines():
      xy = line.split('<')[1]
      xy = xy[:xy.index('>')].split(',')
	  
      vel = line.split('<')[2]
      vel = vel[:vel.index('>')].split(',')
	  
      results.append({
        "x": int(xy[0]),
    	"y": int(xy[1]),
		"vel_x": int(vel[0]),
		"vel_y": int(vel[1])
      })

    return results

	
def plot(points, step, h, w):
  new_p = []
  for p in points:
    new_p.append({
      "x": p["x"] + (p["vel_x"] * step),
	  "y": p["y"] + (p["vel_y"] * step)
    })

  max_x = max(p['x'] for p in new_p)
  max_y = max(p['y'] for p in new_p)
  min_x = min(p["x"] for p in new_p)
  min_y = min(p["y"] for p in new_p)
	
  res = False
  
  # If it fis between the bounds, print it out
  if max_y - min_y <= h and max_x - min_x <= w:
    array = numpy.zeros((h, w))
    res = True
    for p in new_p:
      array[p['y'] - min_y][p['x'] - min_x] = 1

    # Print nicely
    for ar in array:
      print(numpy.array_repr(ar).replace('\n', '').replace('\t', '').replace("      ", "").replace("0.", "  "))

  return res
    

res = parse("input")
step = 1
while not plot(res, step, 10, 100):
  step = step + 1
print("steps:", step)