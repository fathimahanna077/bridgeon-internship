import requests

response = requests.get("https://api.github.com/users/octocat")

if response.status_code == 200:
    user = response.json()

    print("===== GitHub User Info =====")
    print(f"Name         : {user['name']}")
    print(f"Location     : {user['location']}")
    print(f"Public Repos : {user['public_repos']}")
    print(f"Created At   : {user['created_at']}")
else:
    print("Failed to fetch data")