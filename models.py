from extensions import db
from sqlalchemy.orm import validates
import re

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)

    hero_powers = db.relationship('HeroPower', backref='hero', cascade='all, delete-orphan')
    powers = db.relationship('Power', secondary='hero_powers', backref='heroes')

    def __repr__(self):
        return f'<Hero {self.id}, {self.name}, {self.super_name}>'

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

    hero_powers = db.relationship('HeroPower', backref='power', cascade='all, delete-orphan')

    @validates('description')
    def validate_description(self, key, description):
        if not description or len(description) < 20:
            raise ValueError('Description must be present and at least 20 characters long')
        return description

    def __repr__(self):
        return f'<Power {self.id}, {self.name}, {self.description}>'

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    @validates('strength')
    def validate_strength(self, key, strength):
        valid_strengths = ['Strong', 'Weak', 'Average']
        if strength not in valid_strengths:
            raise ValueError('Strength must be one of: Strong, Weak, Average')
        return strength

    def __repr__(self):
        return f'<HeroPower {self.id}, {self.hero_id}, {self.power_id}, {self.strength}>'