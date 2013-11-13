import urllib

origin_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
param = '12345'
count = 0
while count < 400:
    url = origin_url + param
    param = urllib.urlopen(url).read().split()[-1]
    print param
    count += 1

