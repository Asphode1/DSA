from random import randint
from datetime import datetime

arr = [randint(-1000, 1000) for i in range(1000)]

def sumArr(a, i, j):
  sum = 0
  for i in a[i:(j + 1)]:
    sum += i
  return sum

def bruteForce(a):
  l = len(a)
  max = 0
  for i in range(l):
    for j in range(i, l):
      sum = sumArr(a, i, j)
      if(sum > max):
        max = sum
  return max

def betterBruteForce(a):
  l = len(a)
  max = 0
  for i in range(l):
    sum = 0
    for j in range(i, l):
      sum += a[j]
      if(sum > max):
        max = sum
  return max

def maxMid(a, start, end, mid):
  max1 = 0
  sum1 = 0
  for i in range(mid - 1, start - 1, -1):
    sum1 += a[i]
    if(max1 < sum1):
      max1 = sum1
  max2 = 0
  sum2 = 0
  for i in range(mid, end):
    sum2 += a[i]
    if(max2 < sum2):
      max2 = sum2
  return max1 + max2

def recur(a, start, end):
  if(start == end):
    return a[start]
  else:
    mid = int((end + start) / 2)
    max1 = recur(a, start, mid)
    max2 = recur(a, mid + 1, end)
    maxmid = maxMid(a, start, end, mid)
    return max(max1, max2, maxmid)

def dynamic(a):
  smax = a[0]
  ei = a[0]
  for i in range(1, len(a)):
    ei = max(a[i], ei + a[i])
    smax = max(smax, ei)
  return smax

def run(arr, i):
  match i:
    case 1:
      now = datetime.now()
      bruteForce(arr)
      end = datetime.now()
      return format(end - now)
    case 2:
      now = datetime.now()
      betterBruteForce(arr)
      end = datetime.now()
      return format(end - now)
    case 3:
      now = datetime.now()
      dynamic(arr)
      end = datetime.now()
      return format(end - now)

print(run(arr, 1))