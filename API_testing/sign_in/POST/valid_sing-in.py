"""
sign-in user who was in system, with valid email and password
"""
import requests

url = "http://localhost:80/sign-in"

payload = {'email': 'lu@gmail.com',
           'password': '1q2w3E'}
files = [

]
headers = {
  'Content-Type': 'text/html',
  'Cookie': 'remember_token=1'
            '|85298fcf755507c79781b91bdff6de00000a48babae30e3c36b16870233e4651d20fe2410ced339cb1d8d57355c125bf2c4061888cbe4d3f2854403161c61c83; session=.eJwlzj0OwjAMQOG7ZGaI65_EvUzlOLZgTemEuDuVWN72pO9TjlxxPsv-Xlc8yvGaZS-GSRLUeUBtpgQSQ7kPRYKZ1tFzsjYYLsp3ubJ1dc_7mdUmmpvoltE7QlDL5lXU5gDSZiYD0NnIG_LmlsKJUJEUPLSxe7kh1xnrr4Hy_QHrWS_Z.ZYMA4A.VHt2UhhTWAYQegP_7IY7LA-PMAY'
}

response = requests.request("POST", url, data=payload)

print(response.status_code)
