import requests

url = "https://sandbox.onebrick.io/v1/account/list/"

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer public-sandbox-3bc0aff7-dac2-4068-9fc9-082aecabd18b"
}

response = requests.get(url, headers=headers)

print(response.text)