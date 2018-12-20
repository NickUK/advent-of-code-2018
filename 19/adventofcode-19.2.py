Day 19 part 2

def sum_factors(n):
  total = 0
  for i in range(1, n+1):
    if n % i ==0:
      total += i
  return total

print(sum_factors(10551417))