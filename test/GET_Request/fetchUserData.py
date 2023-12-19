"""
first GET test
"""
import requests
import json
import jsonpath

import flask

#  API URL
url = "http://localhost:80"

#  send GET request
response = requests.get(url)
print("start page: {}".format(response))

# print("profile: {}".format(requests.get("http://localhost:80/profile")))
# print("quotes: {}".format(requests.get("http://localhost:80/quotes")))
# print("favorite: {}".format(requests.get("http://localhost:80/favorite")))
# print("home: {}".format(requests.get("http://localhost:80/home")))
# print("sign-in: {}".format(requests.get("http://localhost:80/sign-in")))
# print("sign-up: {}".format(requests.get("http://localhost:80/sign-up")))
# print("quote-life: {}".format(requests.get("http://localhost:80/quote-life")))
# print("quote-travel: {}".format(requests.get("http://localhost:80/quote-travel")))
# print("quote-race: {}".format(requests.get("http://localhost:80/quote-race")))

# Display response content
print(response.content)
print(response.headers)
print(response.headers.get('Date'))  # ?
print(response.headers.get('Server'))  # ?

# fetch cookies
print(response.cookies)

# fetch encoding
print(response.encoding)

print(response.elapsed)
print(response.status_code)

url = "http://localhost:80/sign-in"  # Замените на фактический URL вашего API

# Попытка входа с неверными учетными данными
payload = {'email': 'invalid_username', 'password': 'invalid_password'}
response = requests.post(url, data=payload)

# Проверка, что возвращается код ошибки 403 Forbidden
print("status code: {}".format(response.status_code))
assert response.status_code == 403

print(response.headers)

# Проверка, что в теле ответа содержится ожидаемый текст (опционально)
expected_error_message = "Invalid credentials"
print("!!!!!!!!!!!!!!!!!, {}".format(response.get_flashed_messages()))
assert expected_error_message in get_flash_message()
