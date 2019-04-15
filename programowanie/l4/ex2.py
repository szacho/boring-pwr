import argparse, random, imageio, shutil
import matplotlib.pyplot as plt
from pathlib import Path
from vector import Vector

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', type=float, default=0.5, help="animation interval")
    parser.add_argument('-n', type=int, default=50, help="number of steps")
    parser.add_argument('-s', type=int, default=5, help="size of a board (square)")
    args = parser.parse_args()
    generateGif(args)

def plotStep(v):
    XY = zip(*v)
    plt.plot(*XY, color='magenta')

def vecsum(size, arr):
    it = iter(arr)
    total = next(it)
    yield Vector([0,0]), total
    for el in it:
        prev = total
        total += el
        outOfRange = [*map(lambda s: abs(s) > size, total)]
        if any(outOfRange):
            moveX, moveY = Vector([0,0]), Vector([0,0])
            if outOfRange[0] and total[0] > size:
                moveX = Vector([-2*size,0])
            elif outOfRange[0] and total[0] < -size:
                moveX = Vector([2*size,0])
            if outOfRange[1] and total[1] > size:
                moveY = Vector([0,-2*size])
            elif outOfRange[1] and total[1] < -size:
                moveY = Vector([0,2*size])
            total = total + moveX + moveY
            yield prev+moveX+moveY, total
            continue
        yield prev, total

def generateGif(args):
    interval, size, N = args.t, args.s, args.n
    moves = [[1,0], [0,1], [-1,0], [0,-1], [1,1], [1,-1], [-1,1], [-1,-1]]
    steps = [Vector([0,0])]

    imgDir = Path('images_ex2')
    if not imgDir.exists(): imgDir.mkdir()
    images = []

    for k in range(N):
        steps = [ *steps, Vector(random.choice(moves)) ]

    trace = [ *vecsum(size, steps) ]
    for key, tr in enumerate(trace):
        plt.axis([-size, size, -size, size])
        plt.title(f'steps: {N}, interval: {interval}, size: {size}')
        for i in range(key+1):
            plotStep(trace[i])
        plt.scatter(*trace[key][1], color='black')
        path = Path(f'images_ex2/img_{key}.png')
        plt.savefig(path)
        plt.clf()
        images.append(imageio.imread(path))

    imageio.mimsave(Path('movie.gif'), images, 'GIF', duration=interval)
    shutil.rmtree(imgDir)

if __name__ == '__main__': main()
