# Generated by Django 4.2 on 2023-10-18 06:28

import catalog.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="опубликовано"),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Напишите название",
                        max_length=150,
                        unique=True,
                        verbose_name="название",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Напишите текст для описания",
                        max_length=200,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                regex="[a-zA-Z0-9_-]+"
                            )
                        ],
                        verbose_name="слаг",
                    ),
                ),
                (
                    "weight",
                    models.SmallIntegerField(
                        default=100,
                        help_text="Напишите вес товара",
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(32767),
                        ],
                        verbose_name="вес",
                    ),
                ),
                (
                    "norm_name",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="Это нормализованное имя",
                        max_length=150,
                        verbose_name="нормализованное имя",
                    ),
                ),
            ],
            options={
                "verbose_name": "категория",
                "verbose_name_plural": "категории",
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="опубликовано"),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Напишите название",
                        max_length=150,
                        unique=True,
                        verbose_name="название",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Напишите текст для описания",
                        max_length=200,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                regex="[a-zA-Z0-9_-]+"
                            )
                        ],
                        verbose_name="слаг",
                    ),
                ),
                (
                    "norm_name",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="Это нормализованное имя",
                        max_length=150,
                        verbose_name="нормализованное имя",
                    ),
                ),
            ],
            options={
                "verbose_name": "тег",
                "verbose_name_plural": "теги",
            },
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="опубликовано"),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Напишите название",
                        max_length=150,
                        unique=True,
                        verbose_name="название",
                    ),
                ),
                (
                    "text",
                    models.TextField(
                        help_text="Напишите здесь текст описывающий товар",
                        validators=[
                            catalog.validators.ValidateMustContain(
                                "превосходно", "роскошно"
                            )
                        ],
                        verbose_name="текст",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        help_text="Выберите категорию",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.category",
                        verbose_name="категория",
                    ),
                ),
                ("tags", models.ManyToManyField(to="catalog.tag")),
            ],
            options={
                "verbose_name": "товар",
                "verbose_name_plural": "товары",
            },
        ),
    ]