import subprocess
import sys
from pathlib import Path
from os import walk

if len(sys.argv) < 2:
  sys.exit("please specify a file")

path = Path(sys.argv[1])

allfiles = []
for (_,_,filenames) in walk(path.parent):
  allfiles.extend(filenames)
  break

print(str(path.parent))
files = []
for f in allfiles:
  copy = f
  if copy.lower().endswith(('.mp3','.m4a')):
    files.append(f)

files.sort()
print(files)

isAfter = False
for _ in range(2):
  for f in files:
    if f == path.name:
      if isAfter:
        exit(0)
      isAfter = True
    if isAfter:
      subprocess.run(['vlc', str(path.parent) + "/" + f])
