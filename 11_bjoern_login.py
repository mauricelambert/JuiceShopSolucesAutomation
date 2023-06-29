from urllib.request import urlopen, Request
from json import dumps, load
from base64 import b64encode

email = "bjoern.kimminich@gmail.com"
password = b64encode(email[::-1].encode()).decode()

response = urlopen(
	Request(
		"http://15.236.144.183:8082/rest/user/login",
		data=dumps({
			"email": email,
			"password": password,
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
print(dumps(load(response), indent=4))