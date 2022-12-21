import os
from os import listdir
from os.path import isfile, join
path = ''

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

for j in onlyfiles:
  oldName = f'{path}\\{j}'
  newName = f'{path}\\{j.replace(" algo que você não queira nos nomes", "")}'
  print(newName)
  os.rename(oldName, newName)


print('Finished!')