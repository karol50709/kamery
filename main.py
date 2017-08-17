import os
import fnmatch
import shutil

destination='/home/karol/python'
matches = []
for root, dirnames, filenames in os.walk('/home/karol/Pobrane/'):
    for filename in fnmatch.filter(filenames, '*.txt'):
        matches.append(os.path.join(root, filename))

count=len(matches)
print count

for i in range(len(matches)):
    print (i," ",matches[i])

name = input("Podaj numer pliku ktory chcesz skopiowac ")
print matches[name]
shutil.copy(matches[name], destination)
print "zmiana nazwy pliku na .mtxcopy"
temp=matches[name]+"copy"
print temp
os.rename(matches[name],temp)


