from django.db import models


class ModelsCoreCatalogAndTag(models.Model):
    is_published = models.BooleanField("опубликовано", default=True)
    name = models.CharField(
        "название", unique=True, max_length=150, help_text="Напишите название"
    )

    class Meta:
        abstract = True
