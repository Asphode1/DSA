S = [3, 34, 4, 12, 5, 2]
L = 6

def test(S, n, sum):
  if(n == 0 and sum != 0):
    return
  elif(sum == 0):
    print(True)
    return
  else:
    for i in range(n, -1, -1):
      test(S, n - 1, sum - S[i])

test(S, 5, 9)