from pyScript import main_page, register_page, logout, api
from pyScript.login_manager import login_manager
from configparser import ConfigParser
from pyScript.csrf import csrf
from threading import Thread
from pyScript import monitor
from database.db import db
from database import users
from flask import Flask

app = Flask(__name__)


config = ConfigParser()
config.read('config.ini', encoding='UTF8')


def load_config():
    # config file load
    app.config['SECRET_KEY'] = config['main']['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = config['main']['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['main'].getboolean('SQLALCHEMY_TRACK_MODIFICATIONS')
    app.config['DEBUG'] = config['main'].getboolean('debug')


def load_blueprints():
    # Создал страничку подключил блупринт
    app.register_blueprint(main_page.blueprint)
    app.register_blueprint(register_page.blueprint)
    app.register_blueprint(logout.blueprint)
    app.register_blueprint(api.blueprint)


def load_database():
    # Иницилизировал базу данных
    csrf.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return users.User.query.filter_by(id=user_id).first()


if __name__ == '__main__':
    load_config()
    load_database()
    load_blueprints()
    t1 = Thread(target=monitor.while_function, args=())
    t1.start()
    app.run(config['main']['ip'], int(config['main']['port']))
