import json, re
from itertools import accumulate
from functools import reduce
from operator import add
from cmath import sqrt

with open('l3_data.json') as f:
  data = json.load(f)

print('Zad. 1 i 2')
def generateHistogram(text):
  text = text.lower()
  his = {}
  for letter in text:
    if letter in his:
      his[letter] += 1
    else:
      if re.match('[a-ząćęłńóśźż]', letter):
        his[letter] = 1
  sortedHis = sorted((v, k) for k, v in his.items())[-10:]

  # scaling
  avg = sum([x[0] for x in sortedHis])/len(sortedHis)
  sd = sortedHis[-1][0] - sortedHis[1][0] # standard deviation
  scaledHis = [(x[0], ((x[0]-avg)/sd+1)*10, x[1]) for x in sortedHis]
  for x in scaledHis:
    print(x[-1]+': ', '*'*round(x[1]), x[0])

print('EN')
generateHistogram(data['text_en'])
print('PL')
generateHistogram(data['text_pl'])

print('Zad. 3 i 4')
def rot13(text):
  res = ''
  for ch in text:
    if re.match('[a-zA-z]', ch):
      n = ord(ch)
      if ord('z')-n > 26:
        if n < ord('Z')-13: n+=13
        else: n-=13
      else: 
        if n < ord('z')-13: n+=13
        else: n-=13   
      res += chr(n)
    else: res += ch 
  return res

print(rot13(data['rot_1']))
print(rot13(data['rot_2']))

print('Zad. 5')
gcd = lambda x, y: x if y == 0 else gcd(y, x%y)
multiVarGcd = lambda arr: reduce(gcd, arr) # bo gcd(a, b, c) == gcd(gcd(a, b), c)

print(multiVarGcd([42,30,4]))

print('Zad. 6')
def pascalTriangle(n):
  row = [1]*n
  while n > 0:
    yield row
    n -= 1
    row = list(accumulate(row, add))[:-1]

[print(x) for x in pascalTriangle(6)]


print('Zad. 7')
def findSolutions(a, b, c):
  d = b*b - 4*a*c
  x1, x2 = (-b+sqrt(d))/2*a, (-b-sqrt(d))/2*a 
  return [x1, x2] if x1 != x2 else [x1, '2-krotny']

while True:
  try:
    a, b, c = map(complex, input('Podaj współczynniki trójmianu kwadratowego oddzielone spacją: ').strip().split(' '))
    if a == 0j:
      print('Pierwszy współczynnik powinien być różny od zera')
  except ValueError:
    print('Wprowadzone dane są niepoprawne. Spróbuj ponownie')
  else:
    [print(x) for x in findSolutions(a, b, c)]
    break

  
