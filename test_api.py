import requests

url = "http://127.0.0.1:5000/analyze"
headers = {
    "Content-Type": "application/json",
    "X-Coin-Name": "bitcoin"
}
response = requests.post(url, headers=headers, json={})

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
