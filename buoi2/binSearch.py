from math import floor


a = [6, 13, 14, 25, 33, 43, 51, 53, 64, 72, 84, 93, 95, 96, 97]
l = len(a)
def binSearch(low: int, high: int, lst: list[int], key: int) -> int:
  if low > high:
    return -1
  mid = floor((high + low) / 2)
  if lst[mid] == key:
    return mid
  elif lst[mid] > key:
    return binSearch(low, mid - 1, lst, key)
  else:
    return binSearch(mid + 1, high, lst, key)

print(binSearch(0, l - 1, a, 31))
