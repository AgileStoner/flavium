import requests

tennis_court_id = input('Enter tennis court id: ')

try:
    tennis_court_id = int(tennis_court_id)
except ValueError:
    tennis_court_id = None
    print('Invalid id')

if tennis_court_id is None:

    endpoint = f'http://127.0.0.1:8000/api/venues/tenniscourts/{tennis_court_id}/delete/'

    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code == 204)