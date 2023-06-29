from urllib.request import urlopen, Request
urlopen(
    Request(
    	"http://15.236.144.183:8082/#/score-board",
	    headers = {
	    	"Cookie": (
				"language=en; welcomebanner_status=dismiss;"
				" continueCode=ZaRwEmgxBPbY2oq9vKejJz6AWLU9"
				"TLiKZSrMdpDWVQk837ZrnN1OX5y4lLMD; cookieconsent"
				"_status=dismiss"
			),
		},
	)
)

from os import system
from sys import executable
system(executable + " -m pip install --require-virtualenv selenium > nul")

from selenium.webdriver import Firefox
driver = Firefox()
driver.execute_script('if (document.getElementById("mat-dialog-0")) {document.getElementById("mat-dialog-0").getElementsByTagName("button")[1].click()}')
driver.get("http://15.236.144.183:8082/#/score-board")
driver.close()