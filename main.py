from configparser import ConfigParser
from flask import Flask

app = Flask(__name__)
config = ConfigParser()
config.read('config.ini', encoding='UTF8')


from pyScript import main_page
from pyScript import register_page
# и т.п импорты страниц

app.register_blueprint(main_page.blueprint)
app.register_blueprint(register_page.blueprint)
# Создал страничку подключил блупринт

if __name__ == '__main__':
    app.run(config['main']['ip'], int(config['main']['port']))
