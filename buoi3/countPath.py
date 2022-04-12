def countPath(i, j, d, c):
  if(i == d or j == c):
    return 1
  return countPath(i + 1, j, d, c) + countPath(i, j + 1, d, c)

print(countPath(1, 1, 2, 3))
