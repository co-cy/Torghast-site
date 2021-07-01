from configparser import ConfigParser
from flask import Flask

app = Flask(__name__)

# config file load
config = ConfigParser()
config.read('config.ini', encoding='UTF8')

app.config['SECRET_KEY'] = config['main']['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = config['main']['SQLALCHEMY_DATABASE_URI']
app.config['DEBUG'] = config['main'].getboolean('debug')

from pyScript import main_page, register_page
# и т.п импорты страниц

app.register_blueprint(main_page.blueprint)
app.register_blueprint(register_page.blueprint)
# Создал страничку подключил блупринт

if __name__ == '__main__':
    app.run(config['main']['ip'], int(config['main']['port']))
