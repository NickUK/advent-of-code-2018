# Day 13 part 1+2

import copy


class Registers:
  def __init__(self, r):
    self.r = r

  def __eq__(self, other):
    return self.r == other.r
    
  def __str__(self):
    return "[" + str(self.r) + "]"


class Values:
  def __init__(self, a, b, c):
    self.a = int(a)
    self.b = int(b)
    self.c = int(c)
    
  def __str__(self):
    return "[" + str(self.a) + ", " + str(self.b) + ", " + str(self.c) + "]"

  
def addr(reg, val):
  r = copy.copy(reg.r)
  r[val.c] = reg.r[val.a] + reg.r[val.b]
  return Registers(r)

def addi(reg, val):
  r = copy.copy(reg.r)
  r[val.c] = reg.r[val.a] + val.b
  return Registers(r)

def mulr(reg, val):
  r = copy.copy(reg.r)
  r[val.c] = reg.r[val.a] * reg.r[val.b]
  return Registers(r)

def muli(reg, val):
  r = copy.copy(reg.r)
  r[val.c] = reg.r[val.a] * val.b
  return Registers(r)
  
def banr(reg, val):
  r = copy.copy(reg.r)
  r[val.c] = reg.r[val.a] & reg.r[val.b]
  return Registers(r)
  
def bani(reg, val):
  r = copy.copy(reg.r)
  r[val.c] = reg.r[val.a] & val.b
  return Registers(r)
  
def borr(reg, val):
  r = copy.copy(reg.r)
  r[val.c] = reg.r[val.a] | reg.r[val.b]
  return Registers(r)
  
def bori(reg, val):
  r = copy.copy(reg.r)
  r[val.c] = reg.r[val.a] | val.b
  return Registers(r)
  
def setr(reg, val):
  r = copy.copy(reg.r)
  r[val.c] = reg.r[val.a]
  return Registers(r)
  
def seti(reg, val):
  r = copy.copy(reg.r)
  r[val.c] = val.a
  return Registers(r)
  
def gtir(reg, val):
  r = copy.copy(reg.r)
  r[val.c] = (1 if val.a > reg.r[val.b] else 0)
  return Registers(r)
  
def gtri(reg, val):
  r = copy.copy(reg.r)
  r[val.c] = (1 if reg.r[val.a] > val.b else 0)
  return Registers(r)
  
def gtrr(reg, val):
  r = copy.copy(reg.r)
  r[val.c] = (1 if reg.r[val.a] > reg.r[val.b] else 0)
  return Registers(r)
  
def eqir(reg, val):
  r = copy.copy(reg.r)
  r[val.c] = (1 if val.a == reg.r[val.b] else 0)
  return Registers(r)
  
def eqri(reg, val):
  r = copy.copy(reg.r)
  r[val.c] = (1 if reg.r[val.a] == val.b else 0)
  return Registers(r)
  
def eqrr(reg, val):
  r = copy.copy(reg.r)
  r[val.c] = (1 if reg.r[val.a] == reg.r[val.b] else 0)
  return Registers(r)
  

OP_CODES = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]


def test_instructions(values, registers_before, registers_after):
  res = []
  for op in OP_CODES:
    after = op(registers_before, values)
    if after == registers_after:
      res.append(op)
  return res
  

def read_register(input):
  input = input[input.index("[")+1:-1]
  tmp = input.split(", ")
  return Registers([int(tmp[0]), int(tmp[1]), int(tmp[2]), int(tmp[3])])


# Part 1
options = {}
with open("input") as f:
  before = None
  values = None
  op_code = None
  count = 0
  for line in f.readlines():
    line = line.strip()

    if "Before: " in line:
      before = read_register(line)
    elif "After: " in line:
      after = read_register(line)
      results = test_instructions(values, before, after)
      
      if op_code in options:
        options[op_code] = list(filter(lambda x: x in results, options[op_code]))
      else: 
        options[op_code] = results

      if len(results) >= 3:
        count += 1
    elif len(line) > 0:
      inst = list(map(lambda x: int(x), line.split(" ")))
      values = Values(inst[1], inst[2], inst[3])
      op_code = inst[0]

  print(count) # Part 1
  
  reduced = True
  final = {}
  all_options = sum([len(options[x]) for x in options])
  while reduced:
    reduced = False

    for opt in options:
      if len(options[opt]) == 1:
        final[opt] = options[opt][0]
        options[opt] = []
        reduced = True

    if not reduced:
      for op in OP_CODES:
        count = 0
        last_at = None
        for opt in options:
          if op in options[opt]:
            count += 1
            last_at = opt

        if count == 1:
          final[last_at] = op
      
    for opt in options:
      options[opt] = list(filter(lambda x: x not in map(lambda y: final[y], final), options[opt]))

    if all_options > sum([len(options[x]) for x in options]):
      all_options = sum([len(options[x]) for x in options])
      reduced = True


  with open("input2") as f:
    in_reg = Registers([0, 0, 0, 0])
    for line in f.readlines():
      inst = list(map(lambda x: int(x), line.split(" ")))
      values = Values(inst[1], inst[2], inst[3])
      op_code = inst[0]

      in_reg = final[op_code](in_reg, values)

    print(in_reg.r[0])
  
