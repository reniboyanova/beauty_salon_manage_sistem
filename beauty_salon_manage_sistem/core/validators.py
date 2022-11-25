from django.core import exceptions
from django.core.exceptions import ValidationError

def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Only letters are allowed!')


def validate_image_size(obj):
    filesize = obj.file.size
    megabyte_limit = 5.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError(f"The maximum file size that can be uploaded is {megabyte_limit}MB")