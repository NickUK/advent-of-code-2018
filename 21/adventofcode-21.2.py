# Day 22 part 2

a = 0
seen = set()
last_unique = 0

while True:
  e = a | 65536
  a = 8595037

  while True:
    a = (((a + (e & 255)) & 16777215) * 65899) & 16777215

    if 256 > e:
      if a not in seen:
        seen.add(a)
        last_unique = a
        break
      else:
        print(last_unique)
        exit()
    else:
      e = int(e / 256)