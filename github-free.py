import urllib2
from itertools import product

lst = []
f = open("valid-github.txt", 'w')
for i in product('aeiobcdfghmnprst1234567890', repeat=3):
    name = ''.join(i)
    try:
        urllib2.urlopen('https://github.com/{0}'.format(name))
    except:
        f.write('{0}\n'.format(name))
        lst.append(name)
        print name
