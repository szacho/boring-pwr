import argparse, sys
from datetime import datetime, date
from math import floor

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--year', type=int, default=datetime.now().year, help='year to calculate the date of Easter Sunday for')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

def calc(args):
    y = args.year
    a, b, c = y % 19, floor(y/100), y % 100
    d, e, f = floor(b/4), b % 4, floor((b+8)/25)
    g = floor((b-f+1)/3)
    h = (19*a+b-d-g+15) % 30
    i, k = floor(c/4), c % 4
    l = (32+2*e+2*i-h-k) % 7
    m = floor((a+11*h+22*l)/451)
    p = (h+l-7*m+114) % 31
    day = p+1
    month = floor((h+l-7*m+114)/31)
    return 'Easter Sunday falls on {}\n'.format(date(y, month, day))

if __name__ == '__main__': main()
