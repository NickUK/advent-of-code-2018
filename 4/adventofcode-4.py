# Day 4 part 1+2

import re
import numpy


def read_and_sort(fileName):
  with open(fileName) as f:
    lines = map(lambda x : re.match(r"\[(?P<date>\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] (?P<text>.*)", x).groupdict(), f.readlines())
    return sorted(lines, key=lambda x: x['date'], reverse=False)


def parse(input):
  guards = []
  guardId = 0
  fellAsleep = None
  sleeps = []
  
  for line in input:
    if 'Guard' in line['text']:
      if guardId is not 0:
        if len([i for i in guards if i['id'] == guardId]) == 0:
          guards.append({ 'id': guardId, 'sleeps': sleeps })
        else:
          existing = next(filter(lambda x: x['id'] == guardId, guards))
          for sleep in sleeps:
            existing['sleeps'].append(sleep)
          
      guardId = int(line['text'].split(' ')[1][1:])
      sleeps = []
    elif 'falls asleep' in line['text']:
      fellAsleep = line['date']
    elif 'wakes up' in line['text']:
      sleeps.append({ 
        'start': fellAsleep,
        'mins': int(line['date'].split(':')[1]) - int(fellAsleep.split(':')[1])
      })

  if guardId is not 0:
    if len([i for i in guards if i['id'] == guardId]) == 0:
      guards.append({
        'id': guardId,
        'sleeps': sleeps
      })
    else:
      existing = next(filter(lambda x: x['id'] == guardId, guards))
      for sleep in sleeps:
        existing['sleeps'].append(sleep)

  return guards


def most_sleeps(input):
  res = 0
  prev_max = 0
  for item in input:
    total = 0
    for sleep in item['sleeps']:
      total = total + sleep['mins']
    if total > prev_max:
      res = item['id']
      prev_max = total
  return res


def best_minute(inputs):
  a = numpy.zeros(60)

  for input in inputs:
    for sleep in input['sleeps']:
      start_min = int(sleep['start'].split(':')[1])
      for x in range(start_min, start_min + sleep['mins']):
        a[x] += 1

  a_list = list(a)
  return a_list.index(max(a_list)), max(a_list)


guards = parse(read_and_sort("input"))

most_sleepy = most_sleeps(guards)
most_sleepy_elf = next(filter(lambda x: x['id'] == most_sleepy, guards))
best_min, __ = best_minute( [most_sleepy_elf] )

print(most_sleepy * best_min)
print("-")

big_min, __ = best_minute(guards)

maxa = 0
maxb = 0
id = 0
for elf in guards:
  a, b = best_minute([elf])
  if a == big_min and b > maxb:
    maxb = b
    maxa = a
    id = elf['id']
    
print (maxa * id)
