import argparse, sys, os
from PIL import Image

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str, default='./', help='path to source image')
    parser.add_argument('-s', '--size', type=int, default=128, help='width of a thumbnail in px, height will be auto-scaled', metavar='')
    parser.add_argument('-f', '--filename', type=str, default='auto', help='filename of generated thumbnail', metavar='')
    args = parser.parse_args()
    sys.stdout.write(str(thumbnail(args)))

def thumbnail(args):
    width, inputPath, filename = args.size, args.input, args.filename
    path, file = os.path.split(inputPath)

    if filename is 'auto':
        filename = file.split('.')
        filename[-2] = filename[-2]+'_thumbnail'
        filename = '.'.join(filename)
    else:
        ext = filename.split('.')[-1].lower()
        if ext is not 'jpg' or ext is not 'jpeg':
            filename = filename+'.jpg'

    outputPath = os.path.join(path, filename)

    try:
        im = Image.open(inputPath)
        height = int(width*im.size[1]/im.size[0])
        im.resize((width, height)).save(outputPath, 'JPEG')
    except Exception as e:
        return str(e)+'\n'
    
    return 'Thumbnail has been saved in {}\n'.format(outputPath)

if __name__ == '__main__': main()
