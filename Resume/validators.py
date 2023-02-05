from django.core.validators import ValidationError


def max_value_validator(value):
    if value > 100:
        raise ValidationError('مقدار وارد شده صحیح نمیباشد بیش تر از حد مجاز است')


def min_value_validator(value):
    if value < 0:
        raise ValidationError('مقدار وارد شده صحیح نمیباشد و کوچک تر از حد مجاز است ')