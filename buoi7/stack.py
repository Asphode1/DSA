def check(str: str):
  opens = ['{', '[', '(']
  ends = ['}', ']', ')']
  lst = []
  for char in str:
    if char in opens:
      lst.append(char)
    if char in ends:
      if ends.index(char) != opens.index(lst[-1]):
        return False
      lst.pop()
  if(len(lst)):
    return False
  return True

str = '[{}]({(())})'
print(check(str))
