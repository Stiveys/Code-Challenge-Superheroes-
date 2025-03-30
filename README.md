# Superheroes API

A Flask API for managing superheroes and their superpowers. This API allows you to track heroes, their superpowers, and the strength levels of their powers.

## Features

- Create and manage superheroes
- Track various superpowers
- Assign powers to heroes with strength levels
- RESTful API endpoints
- Data validation

## Technologies Used

- Python
- Flask
- SQLAlchemy
- SQLite

## Database Schema

### Heroes
- id (Integer, Primary Key)
- name (String)
- super_name (String)

### Powers
- id (Integer, Primary Key)
- name (String)
- description (String, must be at least 20 characters long)

### HeroPowers
- id (Integer, Primary Key)
- strength (String, must be one of: 'Strong', 'Weak', 'Average')
- hero_id (Integer, Foreign Key)
- power_id (Integer, Foreign Key)

## Setup Instructions

1. Clone the repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Initialize the database:
   ```bash
   python init_db.py
   ```
5. Seed the database:
   ```bash
   python seed.py
   ```
6. Run the application:
   ```bash
   python app.py
   ```

## API Endpoints

### GET /heroes
Returns a list of all heroes.

Response:
```json
[
  {
    "id": 1,
    "name": "Kamala Khan",
    "super_name": "Ms. Marvel"
  }
]
```

### GET /heroes/:id
Returns a specific hero and their powers.

Response:
```json
{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel",
  "powers": [
    {
      "id": 1,
      "name": "super strength",
      "description": "gives the wielder super-human strengths"
    }
  ]
}
```

### GET /powers
Returns a list of all powers.

Response:
```json
[
  {
    "id": 1,
    "name": "super strength",
    "description": "gives the wielder super-human strengths"
  }
]
```

### GET /powers/:id
Returns a specific power.

Response:
```json
{
  "id": 1,
  "name": "super strength",
  "description": "gives the wielder super-human strengths"
}
```

### PATCH /powers/:id
Updates the description of a power.

Request:
```json
{
  "description": "Updated description that is at least 20 characters long"
}
```

### POST /hero_powers
Creates a new HeroPower association.

Request:
```json
{
  "strength": "Strong",
  "power_id": 1,
  "hero_id": 1
}
```

## Validation Rules

- Power description must be present and at least 20 characters long
- HeroPower strength must be one of: 'Strong', 'Weak', 'Average'

## License

This project is licensed under the MIT License.