def sum(list: list, i: int) -> int:
  l = len(list)
  if(i == 0):
    return list[0]
  else:
    return list[i] + sum(list, i - 1)

a = [1, 2, 3, 4]
print(sum(a, len(a) - 1))
