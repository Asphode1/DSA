from math import floor


rem = [None] * 100
rem[0] = 1
def power(x: int, n: int):
  if(rem[n]):
    return rem[n]
  if(n % 2 == 0):
    if(rem[int(n / 2)]):
      rem[n] = rem[int(n / 2)] * rem[int(n / 2)]
      return rem[n]
    else:
      return power(x, int(n / 2)) * power(x, int(n / 2))
  else:
    return x * power(x, int(n - 1))
print(power(2, 11))

