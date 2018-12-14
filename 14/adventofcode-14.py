# Day 14 part 1+2

from functools import reduce


def part_1(input, iters):
  elf1 = 0
  elf2 = 1
  output = input

  for _ in range(iters + 6):
    score = output[elf1] + output[elf2]

    if score >= 10:
      output.append(int(score / 10))
      output.append(score % 10)
    else:
      output.append(score)

    elf1 = (elf1 + 1 + output[elf1]) % len(output)
    elf2 = (elf2 + 1 + output[elf2]) % len(output)

  return reduce(lambda x, y: str(x) + str(y), output[iters:iters + 10])
  

def part_2(input, search):
  elf1 = 0
  elf2 = 1
  output = input
  found = False
  test_str = ""

  while not found:
    score = output[elf1] + output[elf2]

    if score >= 10:
      output.append(int(score / 10))
      output.append(score % 10)
    else:
      output.append(score)
    test_str = test_str + str(score)

    elf1 = (elf1 + 1 + output[elf1]) % len(output)
    elf2 = (elf2 + 1 + output[elf2]) % len(output)

    test_str =  test_str[-7:]
    if search in test_str:
      found = True

  return len(output) + test_str.index(look) - 7


print(part_1([3, 7], 84601))
print(part_2([3, 7], "084601"))
