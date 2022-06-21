"""
Mai Trung Kiên
20200301
https://github.com/Asphode1/DSA/tree/master/sort/quickSort.py
"""

from math import floor

def partition(l: list[int], s: int, e: int) -> int:
  p = l[e]
  i = s - 1
  for j in range(s, e):
    if(l[j] <= p):
      i += 1
      (l[i], l[j]) = (l[j], l[i])
  (l[i + 1], l[e]) = (l[e], l[i + 1])
  return i + 1


def quickSort(l: list[int], s: int, e: int) -> None:
  if(s >= e):
    return
  p = partition(l, s, e)
  quickSort(l, s, p - 1)
  quickSort(l, p + 1, e)

a = [6, 3, 8, 4, 7, 2, 5, 9, 1]
quickSort(a, 0, len(a) - 1)
print(a)
