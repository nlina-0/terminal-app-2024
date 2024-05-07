import json

# Custom data structure as a dictionary
data = {
    "fish oil": {
        "14to18": 50,
        "19to50": 100,
        "51andup": 200
    },
    "magnesium": {
        "14to18": 50,
        "19to50": 100,
        "51andup": 200
    },
}

# Write data to a JSON file
with open('vitamins_female.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)