from flask import Flask
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    genres = db.Column("genres", db.ARRAY(db.String()), nullable=True)
    seeking_talent = db.Column(db.Boolean(), nullable=False)
    talent_description = db.Column(db.String(500), nullable=True)
    website = db.Column(db.String(500), nullable=True)
    shows = db.relationship('Show', backref='Venue', lazy='dynamic')

    def __repr__(self):
        return '<Venue {}>'.format(self.name)

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(120), nullable=True)
    state = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(120), nullable=True)
    genres = db.Column(db.ARRAY(db.String()), nullable=True)
    image_link = db.Column(db.String(500), nullable=True)
    facebook_link = db.Column(db.String(120), nullable=True)
    seeking_venue = db.Column(db.Boolean(), nullable=True)
    seeking_description = db.Column(db.String(120), nullable=True)
    website = db.Column(db.String(120), nullable=True)
    shows = db.relationship('Show', backref='Artist', lazy=True)

    def __repr__(self):
        return '<Artist {}>'.format(self.name)

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
    __tablename__ = 'Show'

    id = db.Column(db.Integer(), primary_key=True)
    venue_id = db.Column(db.Integer(), db.ForeignKey(Venue.id), nullable=False)
    artist_id = db.Column(db.Integer(), db.ForeignKey(Artist.id),
                          nullable=False)
    start_time = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<Show {}{}>'.format(self.artist_id, self.venue_id)