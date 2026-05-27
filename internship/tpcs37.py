users = {
    "Alice": {"age": 25, "city": "New York"},
    "Bob": {"age": 30, "city": "Chicago"}
}

# Outer loop iterates through user names
for name, info in users.items():
    print(f"User: {name}")

    for key, value in info.items():
        print(f"  - {key}: {value}")