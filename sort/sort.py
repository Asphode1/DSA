from math import floor


def insertionSort(lst: list[int]) -> list[int]:
  a = []
  a.append(lst[0])
  for i in range(1, len(lst)):
    a.append(lst[i])
    for j in range(i, 0, -1):
      if(a[j] > a[j - 1]):
        break
      tmp = a[j]
      a[j] = a[j - 1]
      a[j - 1] = tmp
  return a

def selectionSort(lst: list[int]) -> list[int]:
  a = lst
  for i in range(len(lst)):
    min = lst[i]
    ind = i
    for j in range(i + 1, len(lst)):
      if min > lst[j]:
        min = lst[j]
        ind = j
    tmp = a[i]
    a[i] = a[ind]
    a[ind] = tmp
  return a

def bubbleSort(l: list[int]) -> list[int]:
  a = l
  while(True):
    s = 0
    for i in range(len(l) - 1):
      if(a[i] > a[i + 1]):
        tmp = a[i]
        a[i] = a[i + 1]
        a[i + 1] = tmp
        s += 1
    if(not s):
      break
  return a

def mergeSort(l: list[int], s: int, e: int) -> None:
  if(s >= e):
    return
  m = floor((s + e) / 2)
  mergeSort(l, s, m)
  mergeSort(l, m + 1, e)
  a = l[s:m + 1]
  b = l[m + 1:e + 1]
  ai = bi = 0
  i = s
  while(i <= e):
    if(ai == m - s + 1):
      l[i] = b[bi]
      bi += 1
      i += 1
    elif(bi == e - m):
      l[i] = a[ai]
      ai += 1
      i += 1
    elif(ai <= m - s and bi < e - m):
      if(a[ai] >= b[bi]):
        l[i] = b[bi]
        bi += 1
        i += 1
      else:
        l[i] = a[ai]
        ai += 1
        i += 1


l = [6, 3, 4, 2, 5, 1]
mergeSort(l, 0, 5)
"""
insertionSort(l)
selectionSort(l)
bubbleSort(l)
"""
print(l)
