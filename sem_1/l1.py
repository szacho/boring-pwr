from math import pi, ceil, floor
# Zad.1
5
x = 5
x + 1 # Ta linia kodu wykonuje działanie 5+1, ale nie nadpisuje zmiennej

# W interaktywnej konsoli Pythona na bieżąco otrzymujemy wynik wprowadzanych poleceń
# Aby wyświetlić wynik działania w konsoli systemowej (domyślnie skrypt się uruchamia bez 'logów') można skorzystać z funkcji print() w pythonie 3.x
x = 5
print(x)
# 5
x += 1 
print(x)
# 6

# Zad.2
szer = 13
wys = 12.0
znak = '.'

# szer/2
# 6.5 w Pythonie 3.x albo 6 w Pythonie 2.7
# szer/2.0
# 6.5
# wys/3
# 4.0
# znak*5
# .....
# znak + 5
# error związany z konwersją zupełnie różnych typów danych

# Zad.3 
print(4/3*pi*5**3)

# Zad.4 
def calcSphereVolume(r):
  return 4/3*pi*r**3

# Zad.5
startTime = 6*60*60 + 52*60
s1, s2, s3 = 1.5, 4.8, 1
t1, t2 = 6*60 + 15, 4*60 + 12
endTime = (startTime + (s1+s3)*t1 + s2*t2)/60/60

print('O godzinie {}:{}'.format(floor(endTime), (endTime-floor(endTime))*60))

# Zad.6
[print('*'*i) for i in range(1,5)]

size = 8
for i in range(1, 4):
  print(' '*ceil(size/2-1), '*')
  if i == 1: 
    for j in range(1,4):
      k = i+2
      while k <= size:
        print(' '*floor((size-k)/2), '*'*k)
        k += 2

# Zad.7
lines = [ '  ____', '@/ ,. \@', '( \__/ )', ' \__U_/']
[print(line) for line in lines]
