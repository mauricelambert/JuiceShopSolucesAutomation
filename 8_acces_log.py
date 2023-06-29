from urllib.request import urlopen
from time import strftime, localtime
from http.client import IncompleteRead
response = urlopen("http://15.236.144.183:8082/support/logs")
# try:
# 	print(response.read().decode())
# except IncompleteRead as response:
# 	print(response.partial.decode())
response = urlopen("http://15.236.144.183:8082/support/logs/access.log." + strftime('%Y-%m-%d', localtime()))
# try:
# 	print(response.read().decode())
# except IncompleteRead as response:
# 	print(response.partial.decode())