from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import EmailValidator

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

def clean_email(value):
    validate_email = EmailValidator()
    try:
        validate_email(value)
    except ValidationError:
        raise ValidationError('Email không đúng định dạng')

    return value
