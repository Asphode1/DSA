from datetime import datetime

def dequyC(k, n):
  if(k == 1):
    return n
  elif(k == n):
    return 1
  else:
    return dequyC(k, n - 1) + dequyC(k - 1, n - 1)

ks = [10, 20, 20, 30, 40]
ns = [20, 35, 40, 50, 60]

for i in range(5):
  start = datetime.now()
  dequyC(ks[i], ns[i])
  end = datetime.now()
  print(format(end - start))
