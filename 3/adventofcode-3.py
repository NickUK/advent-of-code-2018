# Day 3 part 1+2

import numpy


class Claim:
  def __init__(self, id, left, top, width, height):
    self.id = id
    self.top = top
    self.left = left
    self.width = width
    self.height = height


def func(claims_text):
  claims, max_width, max_height = parseClaims(claims_text)
  grid = numpy.zeros((max_width, max_height))

  for claim in claims:
    for x in range(claim.left, claim.left + claim.width):
      for y in range(claim.top, claim.top + claim.height):
        grid[x][y] = grid[x][y] + 1
  #print(grid)

  claim_with_no_intersect = None

  for claim in claims:
    claim_overlaps = False
    for x in range(claim.left, claim.left + claim.width):
      for y in range(claim.top, claim.top + claim.height):
        if grid[x][y] != 1:
          claim_overlaps = True
    if not claim_overlaps:
      claim_with_no_intersect = claim.id
  
  return ((numpy.asarray(grid) > 1).sum()), claim_with_no_intersect


def parseClaims(claims_text):
  results = []
  max_height = 0
  max_width = 0

  for claim_text in claims_text:
    split_text = claim_text.split(' ')
    id = int(split_text[0][1:])
    left = int(split_text[2][: split_text[2].index(",") ])
    top = int(split_text[2][split_text[2].index(",")+1: -1])
    width = int(split_text[3][: split_text[3].index("x") ])
    height = int(split_text[3][split_text[3].index("x")+1: ])

    max_height = max(max_height, top + height)
    max_width = max(max_width, left + width)
    
    results.append(Claim(id, left, top, width, height))
  return results, max_width, max_height

def test(input, expected):
  output = func(input)
  print("[" + ("+" if output == expected else "-") + "] " + str(output) + "~" + str(expected))

test(["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"], (4, 3))
	
with open('input') as f:
  claims = f.readlines()
  print(func(claims))