import urllib
import urllib.request

try:
    site=urllib.request.urlopen('http://pudim.com.br')
except urllib.request.URLError:
    print('O site do pudim nao esta disponível')
else:
    print('O site do pudim esta disponível')