# ip public

import urllib

f = urllib.urlopen("http://ip.42.pl/raw")

print "\nip public is = ",f.read()

