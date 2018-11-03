# Zad.2
print('Zad.2')

def findChar(str, ch):
  index = 0
  while index < len(str):
    if str[index] == ch: 
      return index
    index+=1
  return -1

print(findChar('mango', 'g'))
print(findChar('mango', 'x'))

# Zad.3
print('Zad.3')
def findCharFromPos(str, ch, pos):
  while pos < len(str):
    if str[pos] == ch: 
      return pos
    pos += 1
  return -1
  
print(findCharFromPos('pineapple', 'p', 0))
print(findCharFromPos('pineapple', 'p', 1))

# Zad.4
print('Zad.4')
def countChars(str, ch):
  index, n = 0, 0
  while index < len(str):
    if str[index] == ch:
      n+=1
    index+=1
  return n

print(countChars('pineapple', 'p'))
# czas zmierzony w osobnym skrypcie zawierającym tylko tę funkcję
# real    0m0.043s
# user    0m0.020s
# sys     0m0.012s

# Zad.5
print('Zad.5')
def countCharsV2(str, ch):
  return str.count(ch)

print(countCharsV2('pineapple', 'p'))
# real    0m0.041s
# user    0m0.020s
# sys     0m0.004s

# Zad.6
print('Zad.6')
def compareStrings(s1, s2):
  for i, ch in enumerate(s1):
    if ch == s2[i]:
      continue
    else:
      return False
  return True

print(compareStrings('pineapple', 'mango'))
print(compareStrings('mango', 'pineapple'))
print(compareStrings('pineapple', 'pineapple'))

# Zad.7
# generator w tym przypadku pozwoli na wypisanie znacznie większej ilości liczb, bo nie rezerwuje z góry pamięci ram
print('Zad.7')
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

[print(x) for x in fib(12)]
