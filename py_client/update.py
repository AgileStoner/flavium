import requests

endpoint = 'http://127.0.0.1:8000/api/venues/tenniscourts/4/update/'

data = {
    'name': 'Tennis Court 69',
    'address': 'Qibray',
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())