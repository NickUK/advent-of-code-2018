# Day 25 part 1+2

class Constellation:
  def __init__(self, cid, first):
    self.cid = cid
    self.points = [first]

  def add(self, item):
    self.points.append(item)
  
  def is_near(self, other):
    for p in self.points:
      if manhatten(p, other) <= 3:
        return True
    return False

  def near_constellation(self, other):
    for p in self.points:
      for o in other.points:
        if manhatten(p, o) <= 3:
          return True
    return False

  def __str__(self):
    return "(" + str(self.cid) + "," + str(self.points) + ")"

  def __repr__(self):
    return str(self)


def parse(file_name):
  points = set()
  with open(file_name) as f:
    for line in f.readlines():
      p = list(map(lambda x: int(x), line.strip().split(",")))
      points.add((p[0], p[1], p[2], p[3]))  
  return points
  

def manhatten(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]) + abs(a[3] - b[3])


def process(points):
  constellations = []
  cid = 0

  for p in points:
    if len(constellations) == 0:
      constellations.append(Constellation(cid, p))
      cid += 1
    else:
      added = False
      for c in constellations:
        if c.is_near(p):
          c.add(p)
          added = True
          break
    
      if not added:
        constellations.append(Constellation(cid, p))
      cid += 1

  reduced = True
  while reduced:
    reduced = False
    for c in constellations:
      for o in filter(lambda x: x.cid != c.cid, constellations):
        if c.near_constellation(o):
          c.points.extend(o.points)
          o.points = []
          reduced = True

    constellations = list(filter(lambda x: len(x.points) > 0, constellations))

  print(len(constellations))


res = parse("input")
process(res)