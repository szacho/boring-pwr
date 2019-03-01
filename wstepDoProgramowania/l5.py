import re
from math import ceil

# Zad.1
print('Zad.1')
def rgbToHtml(rgb):
    limit = lambda x: min(255, max(x, 0))
    return ('#'+'{:02X}'*3).format(*[limit(c) for c in rgb]) 

examples = [(0,0,0), (1,2,3), (255,255,255), (-20,275,125)]
[print('{} -> {}'.format(e, rgbToHtml(e))) for e in examples]

# Zad.2
print('Zad.2')
def htmlToRgb(htmlColor):
    htmlColor = htmlColor.lower().split('#')[-1]
    hexColor = []
    if len(htmlColor) == 3:
        htmlColor = ''.join([c*2 for c in htmlColor])
    while htmlColor:
        hexColor.append(int(htmlColor[:2], 16))
        htmlColor = htmlColor[2:]
    return tuple(hexColor)

examples = ['#000000', '#00FF7D', 'ffffff', 'fff', '#dad', 'dad', 'ddaadd']
[print('{} -> {}'.format(e, htmlToRgb(e))) for e in examples]

# Zad.3 i 4
print('Zad.3 i 4')
def recFib(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = recFib(n-1)
        seq.append(seq[-1] + seq[-2])
        return seq

def iterFib(n):
    a, b = 0, 1
    seq = []
    while n > 0:
        seq.append(a)
        a, b = b, a+b
        n-=1
    return seq

print(recFib(10))
# Czas zmierzony dla n = 100 poprzez funkcję 'time'
# real    0m0,064s
# user    0m0,043s
# sys     0m0,023s
print(iterFib(10))
# real    0m0,042s
# user    0m0,030s
# sys     0m0,013s
print('Wersja iteracyjna jest szybsza')

# Zad.5
print('Zad. 5')
def isPalindrome(phrase):
    phrase = [k for k in filter(lambda x: re.match('[a-z]', x), str(phrase).lower())] # usuwa spacje i znaki specjalne
    for n in range(ceil(len(phrase)/2)):
        if phrase[n] != phrase[-n-1]:
            return False
    return True

examples = ['Was it a car or a cat I saw?', 'A man, a plan, a canal, Panama!', "No 'x' in Nixon", 'Bruce Lee', 1001]
[print('{} -> {}'.format(e, isPalindrome(e))) for e in examples]

# Zad.6
print('Zad.6')
def isListSorted(lst):
    return sorted(lst) == lst

examples = [[1,2,3,4], [1,3,2,4], ['A', 'a', 'b'], ['A', 'b', 'a']]
[print('{} -> {}'.format(e, isListSorted(e))) for e in examples]

# Zad.7
print('Zad. 7')
def isAnagram(org, test):
    return sorted(test.lower()) == sorted(org.lower())

examples = [['Creative', 'Reactive'], ['elvis', 'lives'], ['test', 'noway']]
[print('{} -> {}'.format(e, isAnagram(*e))) for e in examples]