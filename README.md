# Fyyur 

## Introduction
- Fyyur is a musical venue and artist booking site that facilitates the discovery and bookings of shows between local performing artists and venues. This site lets you list new artists and venues, discover them, and list shows with artists as a venue owner.

## Instructions about running the app
- clone the application `$ git clone https://github.com/jonathanmusila/fyyur.git`
- `$ cd fyyur`
- make a virtual environment `$ virtualenv env`
- activate the env `$ source env/bin/activate`
- install requirements `$ pip3 install -r reuirements.txt`
- create .env file and add code as shown in env_sample
- to create and run migrations `$ flask db init, $ flask db migrate, $ flask db upgrade`
- run the application `$ flask run`