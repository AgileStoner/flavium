import requests
from getpass import getpass

auth_endpoint = 'http://127.0.0.1:8000/api/auth/'
username = input('Username: ')
password = getpass('Password: ')

auth_response = requests.post(auth_endpoint, json={"username": 'asadulla', "password": password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Token {token}"
    }
    endpoint = 'http://127.0.0.1:8000/api/venues/tenniscourts/'

    get_response = requests.get(endpoint)
    print(get_response.json())