from configparser import ConfigParser
from flask import Flask

app = Flask(__name__)
config = ConfigParser()
config.read('config.ini')

from pyScript import MainPage
# и т.п импорты страниц

app.register_blueprint(MainPage.blueprint)
# Создал страничку подключил блупринт

if __name__ == '__main__':
    app.run(config['main']['ip'], int(config['main']['port']))
