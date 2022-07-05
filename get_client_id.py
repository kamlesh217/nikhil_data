import requests

url = "https://sandbox.onebrick.io/v1/auth/token/"

payload = {
    "accessToken": "public-sandbox-3bc0aff7-dac2-4068-9fc9-082aecabd18b",
    "userId": "ea847949-812e-4424-a7b8-2f07685a4708",
    "redirectUrl": "https://www.postman.com/"
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer public-sandbox-3bc0aff7-dac2-4068-9fc9-082aecabd18b"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)