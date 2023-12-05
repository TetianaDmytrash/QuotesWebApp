import request

# api url
url = ""

# send get request
response = request.get(url)
print(response)  # 200

# display response content
print(response.content)
print(response.headers)

