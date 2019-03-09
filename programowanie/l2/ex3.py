import argparse, sys, os, zipfile
from datetime import datetime, date

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, default='./', help='path to a directory you want to archive')
    args = parser.parse_args()
    sys.stdout.write(str(archive(args)))

def archive(args):
    path = args.path
    if not os.path.exists(path):
        raise Exception('Incorrect path')

    dirName = os.path.relpath(path, os.path.join(path, '..'))
    filename = datetime.now().strftime('%Y_%m_%d_')+dirName+'.zip'

    zipf = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(path):
        for file in files:
            pathToFile = os.path.join(root, file)
            relativePath = os.path.relpath(pathToFile, os.path.join(path, '..'))
            zipf.write(pathToFile, relativePath)

    zipf.close()
    return 'Archive has been created in {}\n'.format(os.path.join(os.getcwd(), filename))


if __name__ == '__main__': main()