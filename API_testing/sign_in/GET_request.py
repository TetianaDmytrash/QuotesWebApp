"""
GET request for sign in page
"""
import requests


def get_request():
    """
    GET request to sign in page
    :return:
    """
    url = "http://localhost:80/sign-in"

    payload = {}
    # files = []
    headers = {
        'Content-Type': 'text/html',
        'Cookie': 'remember_token=1'
                  '|85298fcf755507c79781b91bdff6de00000a48babae30e3c36b16870233e4651d20fe2410ced339cb1d8d57355c125bf2c4061888cbe4d3f2854403161c61c83; session=.eJwlzj0OwjAMQOG7ZGaI65_EvUzlOLZgTemEuDuVWN72pO9TjlxxPsv-Xlc8yvGaZS-GSRLUeUBtpgQSQ7kPRYKZ1tFzsjYYLsp3ubJ1dc_7mdUmmpvoltE7QlDL5lXU5gDSZiYD0NnIG_LmlsKJUJEUPLSxe7kh1xnrr4Hy_QHrWS_Z.ZYMA4A.VHt2UhhTWAYQegP_7IY7LA-PMAY'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200
    assert "Sign In" in response.text


def GET_request_google_page():
    """
    test access to main google page
    """

    url = "https://www.google.com/"

    payload = ""
    headers = {
        'Cookie': 'AEC=Ackid1T7JIUwOKazixi0SEAUX05P0vKt00TPKn5tCQ6plBLPVCwedaYGVfM; CONSENT=PENDING+959; SOCS=CAAaBgiA3YisBg; __Secure-ENID=16.SE=rClkpM-ejRTgMXFpHbdadHHWOVFjMQ9RnTOO56NgTjpxWGoVn5Cpr-bpRddYswMSzsIjy80RZQuwOvREi8AFLo0anI09_mYHGuhYwX3aYVDl-csMZPQwkvTkDgSiZXrebzEb_YfpBDgg8F97D9RzSDOmdKXi9xshTPB6yQJB_Ho'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200
    # assert "'Content-Type': 'text/html" in response.headers
    # print(response.headers)
    # print(response.status_code)

#  """
# first GET test
# """
# import requests
# import json
# import jsonpath
#
# import flask
#
# #  API URL
# url = "http://localhost:80"
#
# #  send GET request
# response = requests.get(url)
# print("start page: {}".format(response))
#
# # print("profile: {}".format(requests.get("http://localhost:80/profile")))
# # print("quotes: {}".format(requests.get("http://localhost:80/quotes")))
# # print("favorite: {}".format(requests.get("http://localhost:80/favorite")))
# # print("home: {}".format(requests.get("http://localhost:80/home")))
# # print("sign-in: {}".format(requests.get("http://localhost:80/sign-in")))
# # print("sign-up: {}".format(requests.get("http://localhost:80/sign-up")))
# # print("quote-life: {}".format(requests.get("http://localhost:80/quote-life")))
# # print("quote-travel: {}".format(requests.get("http://localhost:80/quote-travel")))
# # print("quote-race: {}".format(requests.get("http://localhost:80/quote-race")))
#
# # Display response content
# print(response.content)
# print(response.headers)
# print(response.headers.get('Date'))  # ?
# print(response.headers.get('Server'))  # ?
#
# # fetch cookies
# print(response.cookies)
#
# # fetch encoding
# print(response.encoding)
#
# print(response.elapsed)
# print(response.status_code)
#
# url = "http://localhost:80/sign-in"  # Замените на фактический URL вашего API
#
# # Попытка входа с неверными учетными данными
# payload = {'email': 'invalid_username', 'password': 'invalid_password'}
# response = requests.post(url, data=payload)
#
# # Проверка, что возвращается код ошибки 403 Forbidden
# print("status code: {}".format(response.status_code))
# assert response.status_code == 403
#
# print(response.headers)
#
# # Проверка, что в теле ответа содержится ожидаемый текст (опционально)
# expected_error_message = "Invalid credentials"
# print("!!!!!!!!!!!!!!!!!, {}".format(response.get_flashed_messages()))
# assert expected_error_message in get_flash_message()
