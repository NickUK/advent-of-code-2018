# Day 19 part 1

eip = 0
eip_reg = 0
registers = [1, 0, 0, 0, 0, 0]


def parse(test_input):
  global eip_reg

  instructions = []
  with open(test_input) as f:
    first_line = True
    for line in f.readlines():
      line = line.strip()

      if first_line:
        eip_reg = int(line[4:])
        first_line = False
      else:
        split_line = line.split(" ")
        instructions.append((split_line[0], split_line[1:]))

  return instructions


def print_out(orig, name, values):
  global eip, registers
  print("ip={} {} {} {} {}".format(eip, orig, name, values, registers), flush=True)
  #input()


def run_instruction(instruction):
  global eip, registers

  name = instruction[0]
  values = list(map(lambda x: int(x), instruction[1]))
  a = values[0]
  b = values[1]
  c = values[2]

  orig = str(registers)

  registers[eip_reg] = eip

  # Added to solve part 1. Added a halt instruction in front of the only instruction using r[0]
  if name == "halt":
    print_out(orig, name, values)
    exit()
  elif name == "addr":
    registers[c] = registers[a] + registers[b]
  elif name == "addi":
    registers[c] = registers[a] + b
  elif name == "mulr":
    registers[c] = registers[a] * registers[b]
  elif name == "muli":
    registers[c] = registers[a] * b
  elif name == "banr":
    registers[c] = registers[a] & registers[b]
  elif name == "bani":
    registers[c] = registers[a] & b
  elif name == "borr":
    registers[c] = registers[a] | registers[b]
  elif name == "bori":
    registers[c] = registers[a] | b
  elif name == "setr":
    registers[c] = registers[a]
  elif name == "seti":
    registers[c] = a
  elif name == "gtir":
    registers[c] = (1 if a > registers[b] else 0)
  elif name == "gtri":
    registers[c] = (1 if registers[a] > b else 0)
  elif name == "gtrr":
    registers[c] = (1 if registers[a] > registers[b] else 0)
  elif name == "eqir":
    registers[c] = (1 if a == registers[b] else 0)
  elif name == "eqri":
    registers[c] = (1 if registers[a] == b else 0)
  elif name == "eqrr":
    registers[c] = (1 if registers[a] == registers[b] else 0)

  #print_out(orig, name, values)

  eip = registers[eip_reg]
  eip += 1


ins = parse("input")
#print(ins)
print(eip_reg)

while eip <= len(ins)-1:
  run_instruction(ins[eip])

print(registers)