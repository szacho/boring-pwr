import argparse, sys, os
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs="*", type=str, help="convert line endings in these files")
    args = parser.parse_args()
    sys.stdout.write(str(convert(args)))

def convert(args):
    for pathToFile in args.files:
        file = Path(pathToFile)
        if file.is_file():
            content = replaceLineEndings(file.read_bytes())()
            file.write_bytes(content)
        else:
            raise ValueError("Incorrect path")

def replaceLineEndings(content):
    winEnding = b'\r\n'
    unixEnding = b'\n'
    def winToUnix():
        return content.replace(winEnding, unixEnding)
    def unixToWin():
        return content.replace(unixEnding, winEnding)
    return winToUnix if winEnding in content else unixToWin

if __name__ == '__main__': main()
