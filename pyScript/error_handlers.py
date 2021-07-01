class ErrorHandler(Exception):
    errors = {0: 'ОК'}

    def __init__(self, id, advice, *args, lvl=0, **kwargs):
        self.id = id
        self.advice = advice
        self.description = self.errors[id]
        self.lvl = lvl
        self.all_args = args if args else ''
        self.all_kwargs = kwargs if args else ''

    def __str__(self):
        return f"""\n
        {self.id}# {self.transform_lvl(self.lvl)}
        Описание: {self.description}
        Рекомендация: {self.advice}
        Вы передали:
        \t\t\t{self.all_args}
        \t\t\t{self.all_kwargs}"""

    def get_id(self):
        return self.id

    def get_errors(self):
        return self.errors

    def get_advice(self):
        return self.advice

    def get_description(self):
        return self.description

    def get_lvl(self):
        return self.lvl

    @staticmethod
    def transform_lvl(lvl):
        if lvl == 0:
            type_error = 'CRITICAL'
        elif lvl == 1:
            type_error = 'ERROR'
        elif lvl == 2:
            type_error = 'WARNING'
        elif lvl == 3:
            type_error = 'INFO'
        elif lvl == 4:
            type_error = 'DEBUG'
        else:
            type_error = 'UNKNOWN TYPE'

        return type_error

    def get_all_args(self):
        return self.all_args

    def get_all_kwargs(self):
        return self.all_kwargs