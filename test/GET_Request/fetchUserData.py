"""
first GET test
"""
import requests
import json
import jsonpath

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

# parse response to json format
json_response = json.loads(response.text)
print(json_response)

# fetch value using json path
pages = jsonpath.jsonpath(json_response, 'total pages')
print(pages[0])
