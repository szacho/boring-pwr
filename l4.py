from math import factorial, exp, fabs, sqrt
import matplotlib.pyplot as plt
import random

print('Zad. 1')
expr = lambda x: x/100*100-x
errors = [x for x in range (1,51) if expr(x) != 0]
print('Błąd zachodzi dla liczb {} i jest spowodowany skończoną dokładnością komputera'.format(errors))

print('Zad. 2')
X = [10, 2, -2, -10]
myExp = lambda x, n: sum([x**i/factorial(i) for i in range(0, n)])
approxErr = lambda x, n: fabs(1-myExp(x, n)/exp(x))

def plotErrors(X, n):
    N = list(range(0, n+1))
    yArgs = [[approxErr(x, n) for n in N] for x in X]

    for k, x in enumerate(X):
        plt.plot(N, yArgs[k], label='{}'.format(x))

    plt.ylabel('Approx Error')
    plt.yscale('log')
    plt.legend()
    plt.show()

print('Błąd jest większy dla ujemnych x, ponieważ w obliczanej sumie x do nieparzystej potęgi pozostaje ujemny, przez co odejmowany jest dany składnik sumy')
plotErrors(X, 60)


print('Zad. 3')
x = 9.8**201
y = 10.2**199

z1 = sqrt(x*x+y*y)
z2 = y*sqrt((x/y)**2+1)
print(z1, z2)
print('Bezpieczniej jest używać drugiego wyrażenia')


print('Zad. 4')
x = 10**7.4
y = 10**8.5
B = [random.uniform(x,y) for _ in range(100)]

# z treści: a = c = 1 oraz sign(b) zawsze równe 1
sol1 = lambda b: ((-b-sqrt(b*b-4))/2, (-b+sqrt(b*b-4))/2)
sol2 = lambda b: ((-b-sqrt(b*b-4))/2, 1/((-b-sqrt(b*b-4))/2))
for b in B:
    print(sol1(b))
    print(sol2(b))
print('Wzór (1) jest dokładniejszy')