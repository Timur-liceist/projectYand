import re

from django.core import validators as django_validators
from django.core.exceptions import ValidationError
from django.db import models
import transliterate

from catalog.validators import ValidateMustContain
from core import models as core_models


def preparing_norm_name(name):
    input_string = re.sub(r"[^a-zA-Zа-яА-Я0-9_]+", "", name.lower())
    try:
        norm_name = transliterate.translit(
            input_string.lower(),
            reversed=True,
        )
    except transliterate.exceptions.LanguageDetectionError:
        norm_name = input_string.lower()
    return norm_name


class Tag(core_models.ModelsCoreCatalogAndTag):
    slug = models.SlugField(
        "слаг",
        name="slug",
        max_length=200,
        unique=True,
        help_text="Напишите текст для описания",
        validators=[django_validators.RegexValidator(regex="[a-zA-Z0-9_-]+")],
    )
    norm_name = models.CharField(
        "нормализованное имя",
        max_length=150,
        blank=True,
        editable=False,
        help_text="Это нормализованное имя",
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.norm_name = preparing_norm_name(self.name)
        super().save(*args, **kwargs)

    def clean(self):
        items = Tag.objects.filter(norm_name=preparing_norm_name(self.name))
        for i in items:
            if i.id != self.id:
                raise ValidationError("С таким названием уже есть тег")

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"


class Category(core_models.ModelsCoreCatalogAndTag):
    slug = models.SlugField(
        "слаг",
        name="slug",
        max_length=200,
        unique=True,
        help_text="Напишите текст для описания",
        validators=[django_validators.RegexValidator(regex="[a-zA-Z0-9_-]+")],
    )
    weight = models.SmallIntegerField(
        default=100,
        validators=[
            django_validators.MinValueValidator(1),
            django_validators.MaxValueValidator(32767),
        ],
        verbose_name="вес",
        help_text="Напишите вес товара",
    )
    norm_name = models.CharField(
        "нормализованное имя",
        max_length=150,
        blank=True,
        editable=False,
        help_text="Это нормализованное имя",
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.norm_name = preparing_norm_name(self.name)
        super().save(*args, **kwargs)

    def clean(self):
        items = Category.objects.filter(
            norm_name=preparing_norm_name(self.name)
        )  # noqa
        for item in items:
            if item.id != self.id:
                raise ValidationError("С таким названием уже есть категория")

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Item(core_models.ModelsCoreCatalogAndTag):
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="категория",
        help_text="Выберите категорию",
    )
    text = models.TextField(
        "текст",
        validators=[ValidateMustContain("превосходно", "роскошно")],
        help_text="Напишите здесь текст описывающий товар",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
