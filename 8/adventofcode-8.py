# Day 8 part 1+2

from functools import reduce


class ParsedFile:
  def __init__(self, children, meta, value):
    self.children = children
    self.meta = meta
    self.value = value
    

all_meta = []


def parse(input,  pos):
  files = []
  meta = []
  value = 0

  num_files = int(input[pos])
  num_meta = int(input[pos + 1])

  start = pos + 2
  for _ in range(num_files):
    new_file, start = parse(input, start)
    files.append(new_file)

  meta = input[start:start+num_meta]

  # For part 1
  for m in meta:
    all_meta.append(m)

  if num_files == 0:
    value = reduce(lambda a,b: int(a) + int(b), meta)
  else: 
    for ref in map(lambda x: int(x), meta):
      if ref - 1 < len(files):
        value = value + files[ref - 1].value

  return ParsedFile(files, meta, value), start+num_meta


with open("input") as f:
  testinput = f.readlines()[0]
  #testinput = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"

  result, _ = parse(testinput.split(" "), 0)
  print(reduce(lambda a,b: int(a) + int(b), all_meta)) # Part 1
  print(result.value) # Part 2