# Day 20 part 1+2


DIRECTIONS = {
                'N': (0, -1), 
                'S': (0, 1), 
                'E': (1, 0), 
                'W': (-1, 0)
             }


def parse(file_name):
  with open(file_name) as f:
    return f.read()


def expand(regex_iter, rooms, pos, distance):
  initial_pos = pos
  initial_dist = distance
    
  for char in regex_iter:
    if char in DIRECTIONS:
      pos = (pos[0] + DIRECTIONS[char][0], pos[1] + DIRECTIONS[char][1])
      if pos in rooms: 
        distance = rooms[pos]
      else:
        distance += 1
        rooms[pos] = distance
    elif char == '$':
      return rooms
    elif char == '(':
      expand(regex_iter, rooms, pos, distance)
    elif char == ')':
      return None
    elif char == '|':
      pos = initial_pos
      distance = initial_dist


data = parse("input")
start_pos = (0, 0)
result = expand(iter(data), {start_pos: 0}, start_pos, 0)

print(max(result.values())) # Part 1
print(len(list(filter(lambda v: v >= 1000, result.values())))) # Part 2