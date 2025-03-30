#!/usr/bin/env python3

# This script initializes and seeds the database
# It creates the tables and populates them with sample data

from flask import Flask
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower
from random import choice as rc

# Create a Flask app instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with this app
db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    # Create all tables
    print("Creating database tables...")
    db.create_all()

    print("Clearing existing data...")
    # Clear existing data (in reverse order of dependencies)
    HeroPower.query.delete()
    Hero.query.delete()
    Power.query.delete()

    print("Seeding powers...")
    powers = [
        Power(name="super strength", description="gives the wielder super-human strengths"),
        Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
        Power(name="super human senses", description="allows the wielder to use her senses at a super-human level"),
        Power(name="elasticity", description="can stretch the human body to extreme lengths"),
    ]
    db.session.add_all(powers)

    print("Seeding heroes...")
    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
        Hero(name="Janet Van Dyne", super_name="The Wasp"),
        Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
        Hero(name="Carol Danvers", super_name="Captain Marvel"),
        Hero(name="Jean Grey", super_name="Dark Phoenix"),
        Hero(name="Ororo Munroe", super_name="Storm"),
        Hero(name="Kitty Pryde", super_name="Shadowcat"),
        Hero(name="Elektra Natchios", super_name="Elektra"),
    ]
    db.session.add_all(heroes)

    print("Adding powers to heroes...")
    strengths = ["Strong", "Weak", "Average"]
    hero_powers = []
    for hero in heroes:
        power = rc(powers)
        hero_powers.append(
            HeroPower(hero=hero, power=power, strength=rc(strengths))
        )
    db.session.add_all(hero_powers)
    db.session.commit()

    print("Done seeding!")