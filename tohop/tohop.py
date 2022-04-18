from datetime import datetime

d = [[0 for i in range(100)] for j in range(100)]
ks = [10, 20, 20, 30, 40]
ns = [20, 35, 40, 50, 60]

def dequykonho(k, n):
  if(k == 0 or k == n):
    return 1
  return dequykonho(k, n - 1) + dequykonho(k - 1, n - 1)

def dequyconho(k, n):
  if(k == 0 or k == n):
    return 1
  if (d[k][n] != 0):
    return d[k][n]
  else:
    d[k][n] = dequyconho(k, n - 1) + dequyconho(k - 1, n - 1)
    return d[k][n]


for i in range(1):
  start = datetime.now()
  print(dequykonho(ks[1], ns[2]))
  end = datetime.now()
  print(format(end - start))
