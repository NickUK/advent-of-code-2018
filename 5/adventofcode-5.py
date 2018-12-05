# Day 5 part 1+2


def react(a, b):
  return a != b and a.lower() == b.lower()


def reduce_poly(polymer):
  reduced = []
  for unit in polymer:
    if len(reduced) > 0 and react(reduced[-1], unit):
      reduced.pop()
    else:
      reduced.append(unit)
  return reduced


def remove_type(polymer, char):
  return polymer.replace(char.lower(),"").replace(char.upper(),"")


with open("input") as f:
  #polymer = "dabAcCaCBAcCcaDA"
  polymer = f.readlines()[0]

  # part 1  
  print(len(reduce_poly(polymer)))

  # part 2
  unique_chars = ''.join(set(polymer.lower()))
  print(min([len(reduce_poly(remove_type(polymer, c))) for c in unique_chars]))
