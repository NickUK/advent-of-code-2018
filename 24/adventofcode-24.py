# Day 24 part 1+2

import math

DEBUG = False


class Group:
  def __init__(self, id, side, units, hp, ap, attack_type, initiative, weaknesses, immunities):
    self.id = id
    self.side = side
    self.units = units
    self.hp = hp
    self.ap = ap
    self.attack_type = attack_type
    self.initiative = initiative
    self.weaknesses = weaknesses
    self.immunities = immunities

  def __str__(self):
    return "({} - {}\t units:{}\t hp:{}\t ap:{}\t at:{}\t in:{}\twk:{}\t im:{})".format(self.id, self.side.rjust(12), self.units, self.hp, self.ap, self.attack_type, self.initiative, self.weaknesses, self.immunities)

  def __repr__(self):
    return str(self)

  def effective_power(self):
    return self.units * self.ap

  def damage(self, other):
    multiplier = 1
    if self.attack_type in other.weaknesses:
      multiplier = 2
    elif self.attack_type in other.immunities:
      multiplier = 0

    return self.effective_power() * multiplier

  def damage_assessment(self, other):
    damage_ammount = self.damage(other)
    if DEBUG:
      print("{} group {} would deal defending group {} {} damage".format(self.side, self.id, other.id, damage_ammount))

    return damage_ammount


  def inflict_damage(self, other):
    new_units = max(math.ceil(((other.hp * other.units) - self.damage(other)) / other.hp), 0)
    diff = other.units - new_units
    if DEBUG:
      print("{} group {} attacks defending group {}, killing {} units".format(self.side, self.id, other.id, diff))

    other.units = new_units
    return diff


def print_groups_summary(groups):
  immune = sorted(filter(lambda x: x.side == "Immune" and x.units > 0, groups), key=lambda y: (y.id))
  print("Immune system:")
  for im in immune:
    print("Group {} contains {} units".format(im.id, im.units))
  if len(immune) == 0:
    print("No groups remain")

  infection = sorted(filter(lambda x: x.side == "Infection" and x.units > 0, groups), key=lambda y: (y.id))
  print("Infection:")
  for im in infection:
    print("Group {} contains {} units".format(im.id, im.units))
  if len(infection) == 0:
    print("No groups remain")

  print()


def parse(file_name):
  with open(file_name) as f:
    groups = set()
    side = "Immune"
    id = 0
    for line in f.readlines():
      if "Infection:" in line:
        side = "Infection"
        id = 0

      if "(" not in line:
        line = line.replace("points with", "points () with")

      if len(line) > 1 and ":" not in line:
        start = line[:line.index("(")].split(" ")
        middle = line[line.index("(") + 1: line.rfind(")")].split(";")
        last = line[line.rfind(")"):].split(" ")

        units = int(start[0])
        hp = int(start[4])
        ap = int(last[6])
        attack_type = last[7]
        initiative = int(last[11])

        weaknesses = []
        immunities = []
        for bit in middle:
          if "weak to" in bit:
            weaknesses = bit[len("weak to "):].replace(" ", "").split(",")
          else:
            immunities = bit[len("immune to "):].replace(" ", "").split(",")

        id += 1
        groups.add(Group(id, side, units, hp, ap, attack_type, initiative, weaknesses, immunities))

    return groups      


def round(groups):
  if DEBUG:
    print_groups_summary(groups)

  sides_left = list(map(lambda l: l.side, filter(lambda d: d.units > 0, groups)))
  if not ("Immune" in sides_left and "Infection" in sides_left):
    return list(filter(lambda x: x.units > 0, groups))[0].side, sum(map(lambda m: m.units, groups)) # The end

  # Target selection
  target_set = []
  sorted_groups = sorted(groups, key=lambda p: (-p.effective_power(), -p.initiative))

  targetted = set()
  for group in sorted_groups:
    if group.units > 0:
      temp = list(filter(lambda x: x[1] > 0, map(lambda x: (x, group.damage_assessment(x)), filter(lambda x: x.side != group.side and x.units > 0 and (x.id, x.side) not in targetted, sorted_groups))))
      if len(temp) > 0:
        enemies = list(sorted(temp, key=lambda d: (-d[1], -d[0].effective_power(), -d[0].initiative)))
        target_set.append((group, enemies[0][0]))
        targetted.add((enemies[0][0].id, enemies[0][0].side))
      
  if DEBUG:
    print()
  
  # Attack
  total_killed = 0
  for item in sorted(target_set, key=lambda p: (-p[0].initiative)):
    total_killed += item[0].inflict_damage(item[1])

  if total_killed == 0:
    return "Draw", None
  
  return None, None
  

def fight(groups):
  result = None
  hp_left = 0
  while result is None:
    result, hp_left = round(groups)
  
  return result, hp_left


def part2():
  result = None
  boost = 1
  hp_left = 0
  while result != "Immune": 
    boost += 1 
  
    groups = parse("input")
    for group in filter(lambda x: x.side == "Immune", groups):
      group.ap += boost

    result, hp_left = fight(groups)

  print(hp_left)



print(fight(parse("input"))[1]) # Part 1
part2() # Part 2
