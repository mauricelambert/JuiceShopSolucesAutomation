from urllib.request import urlopen
response = urlopen("http://15.236.144.183:8082/rest/user/whoami?callback=anyname")
print(response.read().decode())