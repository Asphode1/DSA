from hashlib import new


def dynamicr(a):
  arr = [a[0]]
  smax = a[0]
  ei = a[0]
  for i in range(1, len(a)):
    newei = max(a[i], ei + a[i])
    newsmax = max(smax, newei)
    if(newsmax == newei):
      if(newei == a[i]):
        arr = [a[i]]
      else:
        arr.append(a[i])
    else:
      arr.append(a[i])
    smax = newsmax
    ei = newei
  return [arr, smax]

def dynamic(a):
  smax = a[0]
  ei = a[0]
  for i in range(1, len(a)):
    ei = max(a[i], ei + a[i])
    smax = max(smax, ei)
  return smax

a = [1, -4, 2, -3, 7, -2, 4, -1, 2]

print(dynamic(a))
print(dynamicr(a))
