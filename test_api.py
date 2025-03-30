import requests
import json

BASE_URL = 'http://localhost:5555'

def test_get_heroes():
    response = requests.get(f'{BASE_URL}/heroes')
    print('GET /heroes Response:')
    print(f'Status Code: {response.status_code}')
    print(json.dumps(response.json(), indent=2))
    print('\n' + '-'*50 + '\n')

def test_get_hero(id):
    response = requests.get(f'{BASE_URL}/heroes/{id}')
    print(f'GET /heroes/{id} Response:')
    print(f'Status Code: {response.status_code}')
    print(json.dumps(response.json(), indent=2))
    print('\n' + '-'*50 + '\n')

def test_get_powers():
    response = requests.get(f'{BASE_URL}/powers')
    print('GET /powers Response:')
    print(f'Status Code: {response.status_code}')
    print(json.dumps(response.json(), indent=2))
    print('\n' + '-'*50 + '\n')

def test_get_power(id):
    response = requests.get(f'{BASE_URL}/powers/{id}')
    print(f'GET /powers/{id} Response:')
    print(f'Status Code: {response.status_code}')
    print(json.dumps(response.json(), indent=2))
    print('\n' + '-'*50 + '\n')

def test_update_power(id, description):
    headers = {'Content-Type': 'application/json'}
    data = {'description': description}
    response = requests.patch(f'{BASE_URL}/powers/{id}', headers=headers, json=data)
    print(f'PATCH /powers/{id} Response:')
    print(f'Status Code: {response.status_code}')
    print(json.dumps(response.json(), indent=2))
    print('\n' + '-'*50 + '\n')

if __name__ == '__main__':
    test_update_power(1, "gives the wielder super-human strengths")

def test_create_hero_power(hero_id, power_id, strength):
    headers = {'Content-Type': 'application/json'}
    data = {
        'hero_id': hero_id,
        'power_id': power_id,
        'strength': strength
    }
    response = requests.post(f'{BASE_URL}/hero_powers', headers=headers, json=data)
    print('POST /hero_powers Response:')
    print(f'Status Code: {response.status_code}')
    print(json.dumps(response.json(), indent=2))
    print('\n' + '-'*50 + '\n')

if __name__ == '__main__':
    print('\n===== Testing Superheroes API =====\n')

    # Test GET /heroes
    test_get_heroes()

    # Test GET /heroes/:id
    test_get_hero(1)  # Existing hero
    test_get_hero(999)  # Non-existent hero

    # Test GET /powers
    test_get_powers()

    # Test GET /powers/:id
    test_get_power(1)  # Existing power
    test_get_power(999)  # Non-existent power

    # Test PATCH /powers/:id
    test_update_power(1, 'Updated description that is at least 20 characters long')  # Valid update
    test_update_power(2, 'Too short')  # Invalid update (too short description)

    # Test POST /hero_powers
    test_create_hero_power(3, 4, 'Strong')  # Valid hero_power
    test_create_hero_power(3, 4, 'Invalid')  # Invalid strength value