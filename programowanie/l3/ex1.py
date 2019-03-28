import argparse, sys, os, json
from pathlib import Path, PurePath

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', type=str, nargs="+", help='list of files to archive')
    args = parser.parse_args()
    sys.stdout.write(str(make_archive(args)))

def make_archive(args):
    content = []
    for filePath in args.files:
        f, p = Path(filePath), PurePath(filePath)
        if f.is_file() and p.name.split('.')[-1] == 'txt':
            content = [*content, (p.name, f.read_text())]
        else:
            raise ValueError('Incorrect path or file extension')

    with open('archive.txt', 'w+') as archive:
        packedContent = json.dumps(content)
        archive.write(packedContent)

    return f"Files {', '.join(args.files)} has been archived"


if __name__ == '__main__': main()
