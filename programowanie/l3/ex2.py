import argparse, sys, os, json
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help='path to archive')
    args = parser.parse_args()
    sys.stdout.write(str(unpack(args)))

def unpack(args):
    raw = Path(args.path)
    if raw.exists():
        archive = json.loads(raw.read_text())
        for file in archive: save(file)
        return 'Successful unpacking'
    else:
        raise ValueError('Incorrect path')

def save(file):
    dir = Path('archive/')
    path = Path(f"archive/{file[0]}")
    if not dir.exists():
        dir.mkdir()
    if path.exists():
        file[0] = f"_{file[0]}"
        save(file)
    else:
        path.write_text(file[1])

if __name__ == '__main__': main()
