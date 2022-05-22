l = 8

def testc(a: list[int], l: int) -> bool:
  for i in range(l):
    if(a[l] - a[i] == l - i or a[l] - a[i] == i - l):
      return False
  return True

def testh(a: list[int], l: int, t: int) -> bool:
  for i in range(l):
    if(a[i] == t):
      return False
  return True

def bt(n: int, a: list[int]) -> None:
  if(n == l):
    print(a)
  else:
    for i in range(l):
      if(testh(a, n, i)):
        a[n] = i
        if(testc(a, n)):
          bt(n + 1, a)

a = [None] * l
bt(0, a)
