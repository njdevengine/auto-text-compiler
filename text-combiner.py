import shutil
import glob

with open("outputfilename.txt", 'wb') as outfile:
    for filename in glob.glob('folderwithtextfiles/*.txt'):
        if filename == outfile:
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)
