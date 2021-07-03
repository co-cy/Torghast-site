from wtforms.validators import ValidationError
from re import search


class Length(object):
    def __init__(self, min_length=0, max_length=-1):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, form, field):
        len_text = len(field.data)

        if len_text < self.min_length:
            raise ValidationError(f'Вы должны написать минимум {self.min_length} символов')
        if 0 <= self.max_length < len_text:
            raise ValidationError(f'Максимум символов - {self.max_length}')
        return


class ComplexPassword(object):
    """
    Validates the password.
    """
    def __init__(self, check_up=True, check_down=True, check_digit=True):
        self.check_up = check_up
        self.check_down = check_down
        self.check_digit = check_digit

    def __call__(self, form, field):
        password = field.data

        if (self.check_up and not search('[A-Z]', password)) or \
                (self.check_down and not search('[a-z]', password)) or \
                (self.check_digit and not search('[0-9]', password)):

            message = f'Пароль должен содержать минимум:'
            added_point = ' '
            if self.check_up:
                message += added_point + '1-н символ A-Z'
                added_point = ', '

            if self.check_down:
                message += added_point + '1-н символ a-z'
                added_point = ', '

            if self.check_digit:
                message += added_point + '1-ну цифру'

            raise ValidationError(message)

        return
