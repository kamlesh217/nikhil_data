import requests

url = "https://sandbox.onebrick.io/v1/auth/clientId=3041/"

payload = {
    "institutionId": 3,
    "username": "ea847949-812e-4424-a7b8-2f07685a4708",
    "password": "zoQTSbHt3l5cHR99xBskpxA5mZWe6e",
    "redirectRefId": "40995"
}
headers = {
    "Accept": "application/json",
    "Authorization": "Bearer public-sandbox-3bc0aff7-dac2-4068-9fc9-082aecabd18b",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response)