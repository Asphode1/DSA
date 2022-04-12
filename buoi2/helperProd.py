def helperProd(list: list, i: int) -> int:
  if(i == len(list) - 1):
    return list[-1]
  else:
    return list[i] * helperProd(list, i + 1)

a = [1, 3, 3, 4]
print(helperProd(a, 0))