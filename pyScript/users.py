from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin
from datetime import datetime
from main import db


class User(db.Model, UserMixin, SerializerMixin):
    """
    id - уникальный индификатор пользователя
    email - уникальная электронная почта пользователя
    nickname - уникальный игровой ник
    balance - универсальная бесплатная валюта
    skin - скин пользователя на серверах (сслыка на файл)
    privilege - привелегия пользователя на серверах
    date_start_privilege - Дата покупки привелегии
    date_end_privilege - Дата конца покупки превилегии
    donat_balance - виртуальная платная валюта
    date_registered - дата регистрации
    ability_edit_prefix - возможность редактировать игровой префикс
    ability_edit_color_prefix - возможность редактировать цвет игрового префикса
    ability_edit_color_text - возможность редактировать цвет игрового текста
    ability_edit_color_nickname - возможность менять цвет игрового ника
    ability_edit_nickname - возможность редактировать никнейм
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)

    email = db.Column(db.String(32), unique=True, index=True, nullable=False)
    nickname = db.Column(db.String(16), unique=True, index=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)

    balance = db.Column(db.Integer, default=0, nullable=False)
    skin = db.Column(db.Integer, default=0, nullable=False)

    # TODO figure out the time zones
    privilege = db.Column(db.Integer, default=0, nullable=False)
    date_start_privilege = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    date_end_privilege = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    donat_balance = db.Column(db.Integer, default=0, nullable=False)
    date_registered = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    ability_edit_prefix = db.Column(db.Boolean, default=False, nullable=False)
    ability_edit_color_prefix = db.Column(db.Boolean, default=False, nullable=False)
    ability_edit_color_text = db.Column(db.Boolean, default=False, nullable=False)
    ability_edit_color_nickname = db.Column(db.Boolean, default=False, nullable=False)
    ability_edit_nickname = db.Column(db.Boolean, default=False, nullable=False)
    ability_set_hd_skin = db.Column(db.Boolean, default=False, nullable=False)

    # buyers_id = db.Column()
    # id_message_in_forum = db.Column()
    # id_ip = db.Column()

    def __init__(self, email: str, nickname: str, password: str,
                 balance: int = None, skin: str = None, privilege: int = None, donat_balance: int = None,
                 ability_edit_prefix: bool = None, ability_edit_color_prefix: bool = None,
                 ability_edit_color_text: bool = None, ability_edit_color_nickname: bool = None,
                 ability_edit_nickname: bool = None, ability_set_hd_skin: bool = None):
        # TODO add validators

        self.email = email
        self.nickname = nickname
        self.password = generate_password_hash(password)

        if balance is not None:
            self.balance = balance

        if skin is not None:
            self.skin = skin

        if privilege is not None:
            self.privilege = privilege

        if donat_balance is not None:
            self.donat_balance = donat_balance

        if ability_edit_prefix is not None:
            self.ability_edit_prefix = ability_edit_prefix

        if ability_edit_color_prefix is not None:
            self.ability_edit_color_prefix = ability_edit_color_prefix

        if ability_edit_color_text is not None:
            self.ability_edit_color_text = ability_edit_color_text

        if ability_edit_color_nickname is not None:
            self.ability_edit_color_nickname = ability_edit_color_nickname

        if ability_edit_nickname is not None:
            self.ability_edit_nickname = ability_edit_nickname

        if ability_set_hd_skin is not None:
            self.ability_set_hd_skin = ability_set_hd_skin

    def set_email(self, new_email: str):
        self.email = new_email

    def set_nickname(self, new_nickname: str):
        self.nickname = new_nickname

    def set_balance(self, new_balance: int):
        self.balance = new_balance

    def add_balance(self, delta_balance: int):
        self.balance += delta_balance

    def set_skin(self, new_skin: str):
        self.skin = new_skin

    def set_privilege(self, new_privilege: int):
        self.privilege = new_privilege

        self.date_start_privilege = datetime.now()
        # TODO add end of privilege
        self.date_end_privilege = datetime.now()

    def set_donat_balance(self, new_donat_balance: int):
        self.donat_balance = new_donat_balance

    def add_donat_balance(self, delta_donat_balance: int):
        self.donat_balance += delta_donat_balance

    def set_ability_edit_prefix(self, new_status: bool):
        self.ability_edit_prefix = new_status

    def set_ability_edit_color_prefix(self, new_status: bool):
        self.ability_edit_color_prefix = new_status

    def set_ability_edit_color_text(self, new_status: bool):
        self.ability_edit_color_text = new_status

    def set_ability_edit_color_nickname(self, new_status: bool):
        self.ability_edit_color_nickname = new_status

    def set_ability_edit_nickname(self, new_status: bool):
        self.ability_edit_nickname = new_status

    def set_ability_set_hd_skin(self, new_status: bool):
        self.ability_set_hd_skin = new_status

    def get_id(self) -> int:
        return self.id

    def check_id(self, other_id: int) -> bool:
        return self.id == other_id

    def get_email(self) -> str:
        return self.email

    def check_email(self, other_email: str) -> bool:
        return self.email == other_email

    def get_nickname(self) -> str:
        return self.nickname

    def check_nickname(self, other_nickname: str) -> bool:
        return self.nickname == other_nickname

    def check_password(self, password: str, need_hashed: bool = False) -> bool:
        if need_hashed:
            return check_password_hash(self.password, generate_password_hash(password))
        else:
            return check_password_hash(self.password, password)

    def get_balance(self) -> int:
        return self.balance

    def get_skin(self) -> str:
        return self.skin

    def get_privilege(self) -> int:
        return self.privilege

    def get_date_start_privilege(self) -> datetime:
        return self.date_start_privilege

    def get_date_end_privilege(self) -> datetime:
        return self.date_end_privilege

    def get_donat_balance(self) -> int:
        return self.donat_balance

    def get_date_registered(self) -> datetime:
        return self.date_registered






