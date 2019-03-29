import argparse, os, sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-Q', type=float, default=2, help='param Q')
    parser.add_argument('-w', type=float, default=2/3, help='param w')
    parser.add_argument('-A', type=float, default=0.1, help='param A')
    parser.add_argument('-v', type=float, default=0, help='starting velocity')
    parser.add_argument('-th', type=float, default=2, help='starting theta')
    args = parser.parse_args()
    pendulum(args)

def pendulum(args):
    params = (args.A, args.Q, args.w)
    x0 = [args.th, args.v]
    t = np.linspace(0, 10, 1000)
    X = odeint(deriv, x0, t, args=params)

    plotSolution(X, t)
    animation(X[:,0], t)

def animation(X, t):
    fig, ax = plt.subplots()
    xdata, ydata = [], []
    ln, = plt.plot([], [])
    plt.axis('equal')

    def init():
        lim = 1.5
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        return ln,

    def update(i):
        x = [0, np.sin(X[i])]
        y = [0, -np.cos(X[i])]
        ln.set_data(x, y)
        return ln,

    ani = FuncAnimation(fig, update, frames=len(t), interval=5, blit=True, init_func=init)
    plt.show()

def plotSolution(X, t):
    plt.plot(t, X[:,0], label='theta')
    plt.plot(t, X[:,1], label='velocity')
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Solution')
    plt.show()

    plt.plot(X[:,0], X[:,1])
    plt.axis('equal')
    plt.xlabel('Theta')
    plt.ylabel('Velocity')
    plt.show()

def deriv(x, t, A, Q, w):
    theta, v = x[0], x[1]
    return [v, A*np.cos(w*t)-v/Q-np.sin(theta)]

if __name__ == '__main__': main()
