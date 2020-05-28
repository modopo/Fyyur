from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def db_setup(app):
    app.config.from_object('config')
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    return db

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
    genres = db.Column(db.ARRAY(db.String()), nullable=True)
    seeking_talent = db.Column(db.Boolean(), nullable=False)
    talent_description = db.Column(db.String(500), nullable=True)
    website = db.Column(db.String(500), nullable=True)
    shows = db.relationship('Show', backref='Venue', lazy='dynamic')

    def __init__(self, name, city, state, address, phone, image_link,
                 facebook_link, genres, website, seeking_talent = False,
                 talent_description = ""):
        self.name = name
        self.city = city
        self.state = state
        self.address = address
        self.phone = phone
        self.image_link = image_link
        self.facebook_link = facebook_link
        self.genres = genres
        self.website = website
        self.seeking_talent = seeking_talent
        self.talent_description = talent_description

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def shortDescription(self):
        return {
            'id' : self.id,
            'name' : self.name
        }

    def longDescription(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'city' : self.city,
            'state' : self.state
        }

    def detailed(self):
        return {
            'id': self.id,
            'name': self.name,
            'genres': self.genres,
            'address': self.address,
            'city': self.city,
            'phone': self.phone,
            'website': self.website,
            'facebook_link': self.facebook_link,
            'seeking_talent': self.seeking_talent,
            'talent_description': self.talent_description,
            'image_link': self.image_link
        }


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

    def __init__(self, name, city, state, website, phone, genres, image_link,
                 facebook_link, seeking_venue = False, seeking_description
                 =""):
        self.name = name
        self.city = city
        self.state = state
        self.phone = phone
        self.genres = genres
        self.image_link = image_link
        self.facebook_link = facebook_link
        self.seeking_venue = seeking_venue
        self.seeking_description = seeking_description
        self.website = website

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def shortDescription(self):
        return {
            'id' : self.id,
            'name' : self.name
        }

    def detailed(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'genres' : self.genres,
            'city' : self.city,
            'state' : self.state,
            'phone' : self.phone,
            'website' : self.website,
            'facebook_link': self.facebook_link,
            'seeking_talent': self.seeking_talent,
            'seeking_description': self.seeking_description,
            'image_link': self.image_link
        }


# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
    __tablename__ = 'Show'

    id = db.Column(db.Integer(), primary_key=True)
    venue_id = db.Column(db.Integer(), db.ForeignKey(Venue.id), nullable=False)
    artist_id = db.Column(db.Integer(), db.ForeignKey(Artist.id),
                          nullable=False)
    start_time = db.Column(db.String(), nullable=False)

    def __init__(self, venue_id, artist_id, start_time):
        self.venue_id = venue_id
        self.artist_id = artist_id
        self.start_time = start_time

    def insert(self):
        db.session.add(self)
        db.sesions.commit()

    def detailed(self):
        return {
            'venue_id' : self.venue_id,
            'venue_name' : self.Venue.name,
            'artist_id' : self.artist_id,
            'artist_name' : self.Artist.name,
            'artist_image_link' : self.Artist.image_link,
            'start_time' : self.start_time
        }

    def artist_detail(self):
        return {
            'artist_id' : self.venue_id,
            'artist_name' : self.Artist.name,
            'artist_image_link' : self.Artist.image_link,
            'start_time' : self.start_time
        }

    def venue_details(self):
        return {
            'venue_id' : self.venue_id,
            'venue_name' : self.Venue.name,
            'venue_image_link' : self.Venue.image_link,
            'start_time' : self.start_time
        }