import argparse, sys, os, csv, json
from datetime import datetime

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('path', type=str, default='./', help='path to a directory you want stats for')
	parser.add_argument('-s', '--save', action='store_true', help='save into csv file')
	args = parser.parse_args()
	sys.stdout.write(str(scan(args)))

def sortArrayByValue(arr, val):
	return sorted(arr, key=lambda k: k[val], reverse=True)

def saveToFile(filename, stats):
	with open(filename, mode='w') as statsFile:
		fieldnames = ['lastModified', 'filename', 'size', 'relativePath']
		w = csv.DictWriter(statsFile, fieldnames=fieldnames)
		w.writeheader()

		for year in sorted(stats.keys(), reverse=True):
			for file in stats[year]:
				w.writerow(file) 

def scan(args):
	path = args.path
	stats = {}
	for root,dirs,files in os.walk(path):
		for file in files:
			pathToFile = os.path.join(root,file) 
			statinfo = os.stat(pathToFile)

			modified = datetime.fromtimestamp(statinfo.st_ctime)
			year = modified.year
			size = round(statinfo.st_size/1e+6, 2)
			relPath = os.path.relpath(pathToFile, os.path.join(path, '..'))

			entry = { 'lastModified': modified, 'filename': file, 'size': size, 'relativePath': relPath}
			if modified.year in stats:
				stats[year] = [*stats[year], entry]
			else:
				stats[year] = [entry]
			
	for key, val in stats.items():
		stats[key] = sortArrayByValue(val, 'lastModified')
	
	if args.save: 
		output = os.path.relpath(path, os.path.join(path, '..'))+'.csv'
		saveToFile(output, stats)
		return "Stats file has been saved as {}\n".format(output)
	else:
		return str(stats)+'\n'

if __name__ == '__main__': main()