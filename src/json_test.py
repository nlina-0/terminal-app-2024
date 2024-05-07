import json

# Custom data structure as a dictionary
data = {
    "name": "Alice",
    "age": 25,
    "address": {
        "city": "London",
        "country": "UK"
    },
    "hobbies": ["reading", "painting"]
}

# Write data to a JSON file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)