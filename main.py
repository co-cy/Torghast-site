from pyScript import main_page, register_page, logout, api
from pyScript.login_manager import login_manager
from pyScript.csrf import csrf
from threading import Thread
from pyScript import monitor, personal_account, our_servers, server_info
from database.db import db
from database import users
from flask import Flask
from json import load

app = Flask(__name__)


with open('config.json') as file:
    config = load(file)


def load_config():
    # config file load
    app.config.update(SECRET_KEY=config['SECRET_KEY'],
                      SQLALCHEMY_DATABASE_URI=config['SQLALCHEMY_DATABASE_URI'],
                      SQLALCHEMY_TRACK_MODIFICATIONS=config['SQLALCHEMY_TRACK_MODIFICATIONS'],
                      DEBUG=config['debug_mode'],
                      SQLALCHEMY_POOL_SIZE=6)


def load_blueprints():
    # Создал страничку подключил блупринт
    app.register_blueprint(main_page.blueprint)
    app.register_blueprint(register_page.blueprint)
    app.register_blueprint(logout.blueprint)
    app.register_blueprint(api.blueprint)
    app.register_blueprint(personal_account.blueprint)
    app.register_blueprint(our_servers.blueprint)
    app.register_blueprint(server_info.blueprint)


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


@app.context_processor
def info_all_servers():
    return dict(info=monitor.info_all_servers())


if __name__ == '__main__':
    load_config()
    load_database()
    load_blueprints()
    t1 = Thread(target=monitor.endless_checking_servers, args=(config, ))
    t1.start()
    app.run(config['ip'], int(config['port']))
