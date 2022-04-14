def hnt(i: int, a: list, b: list, c: list) -> None:
  if(i == 1):
    c.append(a[len(a) - 1])
    a.pop(-1)
  else:
    hnt(i - 1, a, c, b)
    hnt(1, a, b, c)
    hnt(i - 1, b, a, c)
    print(c)

a = [5, 4, 3, 2, 1]
b = []
c = []

hnt(5, a, b, c)
