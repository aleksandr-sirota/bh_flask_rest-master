from .app import app
from .brand import *
from .car import *
from .color import *


@app.route('/')
def hello_world():
    return 'Привет из Flask! Если ты это видишь, то ты делаешь что-то правильно!'


@app.route('/orm')
def orm():
    return 'Все запросы будут обрабатываться с помощью ORM'


@app.route('/core')
def core():
    return 'Будут выполняться сырые запросы'
