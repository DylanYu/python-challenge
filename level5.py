import sys
import urllib
import pickle

obj = pickle.load(urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))
print obj
for line in obj:
    print ''.join(ch * count for ch, count in line)
