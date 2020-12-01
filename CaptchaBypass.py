import requests
import json

browser = requests.Session()

browser.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
						'Accept': 'application/json, text/plain, */*'})
nLoop = 0
while True:

	jsonCaptcha = json.loads(browser.get("http://localhost:3000/rest/captcha/").text)

	print(jsonCaptcha)

	captchaId = jsonCaptcha['captchaId']
	resposta = jsonCaptcha['answer']

	print(captchaId,resposta)

	dataPostCaptcha = {"UserId":"1","captchaId":captchaId,"captcha":resposta,"comment":"TEST" + str(nLoop),"rating":0}

	jsonResultado = json.loads(browser.post("http://localhost:3000/api/Feedbacks/",dataPostCaptcha).text)

	nLoop += 1

	print(nLoop)
