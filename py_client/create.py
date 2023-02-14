import requests

endpoint = 'http://127.0.0.1:8000/api/venues/tenniscourts/'

data = {
    'name': 'Tennis Court 1',
    'address': 'Tashkent',
    'district': 'OL',
    'phone': '977777777',
    'description': 'Tennis Court 1',
    'price': 100,
    'opens_at': '09:00:00',
    'closes_at': '18:00:00',
    'surface': 'H',
    'indoor': False,
    'lights': True,
    'court_count': 1
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())