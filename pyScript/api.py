from flask import Blueprint, request, jsonify
from database.users import User

blueprint = Blueprint('api', __name__)


@blueprint.route('/api/check_user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def check_user():
    print(1)
    print(request.is_json)
    if not request.is_json:
        return jsonify(error="Неверный формат запроса, обратитесь к администратору")

    json = request.get_json()
    print(json)
    if not json.get('apiKey', False):
        return jsonify(error="Ключ отсутствует, обратитесь к администратору")

    if not json.get('username', False):
        return jsonify(error="Ошибка проверки ника, обратитесь к администратору")

    if not json.get('password', False):
        return jsonify(error="Ошибка проверки пароля, обратитесь к администратору")

    if not json.get('ip', False):
        return jsonify(error="Ошибка проверки доп.инф, обратитесь к администратору")

    # TODO create apiKey
    if json['apiKey'] != 'yourKey':
        return jsonify(error="Неверный ключ, обратитесь к администратору")

    user = User.query.filter_by(nickname=json['username']).first()
    if not user:
        return jsonify(error='Пользователь с таким ником не найден')

    if not user.check_password(json['password']):
        return jsonify(error='Неверный пароль')

    # TODO ip check
    return jsonify(username=user.get_nickname(), permissions=user.get_permissions())


@blueprint.route('/api/get_url', methods=['POST'])
def get_url():
    if not request.is_json:
        return jsonify(error="Неверный формат запроса, обратитесь к администратору")

    json = request.get_json(force=True)

    if not json.get('apiKey', False):
        return jsonify(error="Ключ отсутствует, обратитесь к администратору")

    if not json.get('username', False):
        return jsonify(error="Ошибка проверки ника, обратитесь к администратору")

    if not json.get('password', False):
        return jsonify(error="Ошибка проверки пароля, обратитесь к администратору")

    if not json.get('ip', False):
        return jsonify(error="Ошибка проверки доп.инф, обратитесь к администратору")

    if json['apiKey'] != 'yourKey':
        return jsonify(error="Неверный ключ, обратитесь к администратору")

    if json.get('username', False):
        user = User.query.filter_by(nickname=json['username']).first()
    elif json.get('uuid', False):
        user = User.query.filter_by(uuid=json['uuid']).first()
    else:
        return jsonify(error="Невозможно проверить логин, обратитесь к администратору")

    return jsonify(username=user.get_nickname(), uuid=user.get_uuid(),
                   accessToken=user.get_accessToken(), serverId=user.get_serverId())


@blueprint.route('/api/update_auth_url', methods=['POST'])
def update_auth_url():
    if not request.is_json:
        return jsonify(error="Неверный формат запроса, обратитесь к администратору")

    json = request.get_json(force=True)

    if json.get('accessToken', False):
        return jsonify(error="Ошибка проверки токена обратитесь к администратору")

    if json.get('serverId', False):
        return jsonify(error="Ошибка проверки id, обратитесь к администратору")

    if json.get('username', False):
        user = User.query.filter_by(nickname=json['username']).first()
    elif json.get('uuid', False):
        user = User.query.filter_by(uuid=json['uuid']).first()
    else:
        return jsonify(error="Невозможно проверить логин, обратитесь к администратору")

    user.set_nickname(json['username'])
    user.set_uuid(json['uuid'])
    user.set_accessToken(json['accessToken'])

    return jsonify(state='OK')


@blueprint.route('/api/update_server_id_url', methods=['POST'])
def update_server_id_url():
    if not request.is_json:
        return jsonify(error="Неверный формат запроса, обратитесь к администратору")

    json = request.get_json(force=True)

    if json.get('serverId', False):
        return jsonify(error="Ошибка проверки id, обратитесь к администратору")

    if not json.get('uuid', False):
        return jsonify(error="Невозможно проверить логин, обратитесь к администратору")
    user = User.query.filter_by(nickname=json['username']).first()

    user.set_serverId(json['serverId'])

    return jsonify(state='OK')