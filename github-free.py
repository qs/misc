import urllib2
from itertools import product

lst = []
f = open("valid-github.txt", 'w')
for i in product('aeiobcdfghmnprst1234567890', repeat=3):
    try:
        urllib2.urlopen('https://github.com/%s' % ''.join(i))
    except:
        f.write('%s\n' % ''.join(i))
        lst.append(''.join(i))
        print ''.join(i)
