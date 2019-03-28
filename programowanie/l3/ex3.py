import argparse, os, sys, shutil, time
from pathlib import Path, PurePath
from datetime import date

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=str, help='path to a directory', required=True)
    parser.add_argument('-e', '--extension', type=str, help='extension of files to backup, e.g. txt (w/o period)', required=True)
    args = parser.parse_args()
    sys.stdout.write(str(backup(args)))

def backup(args):
    files = sorted(Path(args.path).glob(f'**/*.{args.extension}'))
    dest = Path(f'Backup/copy-{str(date.today())}/')
    if not dest.exists():
        dest.mkdir(parents=True)
    for file in files:
        daysOld = (time.time()-file.stat().st_mtime)/60/60/24
        if daysOld < 3:
            copy(file, PurePath(dest).joinpath(file.name))
    return 'Successful backup'

def copy(file, dest):
    if Path(dest).exists():
        copy(file, renameFile(dest))
    else:
        shutil.copy(file, dest)

def renameFile(dest):
    filename = f"_{str(dest.name)}"
    return dest.parent.joinpath(filename)

if __name__ == '__main__': main()
