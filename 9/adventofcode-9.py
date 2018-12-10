# Day 9 part 1+2

import numpy
from collections import deque


def marbles(num_players, last_marble):  
  marbles = deque([0])
  elfscores = numpy.zeros((num_players))
  
  for marble_num in range(1, last_marble + 1):
    player = marble_num % num_players

    if marble_num % 23 == 0:
      marbles.rotate(7)
      elfscores[player] += (marble_num + marbles.pop())
      marbles.rotate(-1)
    else:
      marbles.rotate(-1)
      marbles.append(marble_num)
    
    #print(player, marbles)

  return max(elfscores)


def test_marbles(num_players, last_marble, highscore):
  res = marbles(num_players, last_marble)
  pm = "[-]"
  if res == highscore:
    pm = "[+]"
  print(pm, num_players, "players with last marble worth: ", last_marble, " - Expected: ", highscore, " actual:", res)


print(marbles(9, 25))
test_marbles(10, 1618, 8317)
test_marbles(13, 7999, 146373)
test_marbles(17, 1104, 2764)
test_marbles(21, 6111, 54718)
test_marbles(30, 5807, 37305)
print(marbles(424, 71482)) # Part 1
print(marbles(424, 71482*100)) # Part 2