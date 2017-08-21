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
    print i," ",matches[i]

name = input("Podaj numery plikow ktore chcesz skopiowac, oddzielaj numery przecinkiem ',' ")
namestring=str(name)
tabnum=namestring.split(",")
for x in tabnum:
    temps = x.strip("() ")
    i=int(temps)
    shutil.copy(matches[i], destination)
    print "skopiowano plik:     ", matches[i]
    temp=matches[i]+"copy"
    os.rename(matches[i], temp)
    print  "zmieniono nazwe na: ", temp

print "Koniec"