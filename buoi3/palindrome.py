def palindrome(str, i, l):
  if(i > l - 1 - i):
    return True
  if(str[i] == str[l - 1 - i]):
    return palindrome(str, i + 1, l)
  else:
    return False

str = 'madam'

print(palindrome(str, 0, len(str)))
