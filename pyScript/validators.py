from wtforms.validators import ValidationError


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
