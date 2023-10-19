import re

from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class ValidateMustContain(BaseValidator):
    def __init__(self, *must_contain):
        self.must_contain = must_contain

    def __call__(self, a):
        pattern = r"[\W\s]+"
        a = re.split(pattern, a.lower())
        if all(phrase not in a for phrase in self.must_contain):
            raise ValidationError(
                (
                    f"Текст должен содержать хотя бы одно "
                    f"из слов из списка {self.must_contain}."
                )
            )
