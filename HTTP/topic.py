import requests

data = {
    "name": "Hanna",
    "email": "hanna@example.com"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=data
)

print(response.json())