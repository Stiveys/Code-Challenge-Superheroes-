from flask import Flask, request, jsonify
from extensions import db, migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

from models import Hero, Power, HeroPower

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the Superheroes API!'})

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    heroes_data = [{'id': hero.id, 'name': hero.name, 'super_name': hero.super_name} for hero in heroes]
    return jsonify(heroes_data)

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({'error': 'Hero not found'}), 404

    hero_powers = [{
        'id': hp.id,
        'hero_id': hp.hero_id,
        'power_id': hp.power_id,
        'strength': hp.strength,
        'power': {
            'id': hp.power.id,
            'name': hp.power.name,
            'description': hp.power.description
        }
    } for hp in hero.hero_powers]

    hero_data = {
        'id': hero.id,
        'name': hero.name,
        'super_name': hero.super_name,
        'hero_powers': hero_powers
    }
    return jsonify(hero_data)

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    powers_data = [{'id': power.id, 'name': power.name, 'description': power.description} for power in powers]
    return jsonify(powers_data)

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404
    return jsonify({'id': power.id, 'name': power.name, 'description': power.description})

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404

    data = request.get_json()
    try:
        if 'description' in data:
            power.description = data['description']
        db.session.commit()
        return jsonify({'id': power.id, 'name': power.name, 'description': power.description})
    except ValueError as e:
        return jsonify({'errors': [str(e)]}), 400

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()

    # Validate required fields
    if not all(key in data for key in ['strength', 'hero_id', 'power_id']):
        return jsonify({'errors': ['strength, hero_id and power_id are required']}), 400

    # Check if hero and power exist
    hero = Hero.query.get(data['hero_id'])
    if not hero:
        return jsonify({'errors': ['Hero not found']}), 404

    power = Power.query.get(data['power_id'])
    if not power:
        return jsonify({'errors': ['Power not found']}), 404

    try:
        hero_power = HeroPower(
            strength=data['strength'],
            hero_id=data['hero_id'],
            power_id=data['power_id']
        )
        db.session.add(hero_power)
        db.session.commit()

        return jsonify({
            'strength': hero_power.strength,
            'power_id': hero_power.power_id,
            'hero_id': hero_power.hero_id
        }), 201
    except ValueError as e:
        return jsonify({'errors': [str(e)]}), 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)