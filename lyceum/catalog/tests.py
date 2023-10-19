import django.core.exceptions as django_exceptions
from django.test import TestCase

from catalog.models import Category, Item, Tag


class ClassTestCaseItemList(TestCase):
    def test_item_list(self):
        response = self.client.get("/catalog/")
        self.assertEqual(response.status_code, 200)


class ClassTestCaseItemDetail(TestCase):
    def test_item_detail(self):
        response = self.client.get("/catalog/1/")
        self.assertEqual(response.status_code, 200)
        response = self.client.get("/catalog/gflkgjdlkf/")
        self.assertEqual(response.status_code, 404)


class ClassTestCaseRePathCatalog(TestCase):
    def test_catalog_re_path(self):
        response = self.client.get("/catalog/re/123/")
        self.assertEqual(response.status_code, 200)
        response = self.client.get("/catalog/re/-123/")
        self.assertEqual(response.status_code, 404)
        response = self.client.get("/catalog/re/dskjfljs")
        self.assertEqual(response.status_code, 404)


class ClassTestCaseConverterCatalog(TestCase):
    def test_catalog_re_path(self):
        response = self.client.get("/catalog/converter/123/")
        self.assertEqual(response.status_code, 200)
        response = self.client.get("/catalog/converter/-123/")
        self.assertEqual(response.status_code, 404)
        response = self.client.get("/catalog/converter/dskjfljs/")
        self.assertEqual(response.status_code, 404)


class ClassTestCaseCatalogDataBase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            is_published=True,
            name="Тестовое имя",
            slug="test-category-slug",
            weight=100,
        )
        cls.tag = Tag.objects.create(
            is_published=True,
            name="Тестовое имя",
            slug="test-tag-slug",
        )

    def test_data_base_catalogitem(self):
        last_count = Item.objects.count()
        item = Item(
            is_published=True,
            name="Item6",
            text="превосходно",
            category=self.category,
        )
        item.full_clean()
        item.save()
        item.tags.add(self.tag)
        new_count = Item.objects.count()
        self.assertEqual(last_count + 1, new_count)

        last_count = Item.objects.count()
        with self.assertRaises(django_exceptions.ValidationError):
            item = Item(
                is_published=True,
                name="Item6",
                text="плохо работает",  # noqa
                category=self.category,
            )
            item.full_clean()
            item.save()
            item.tags.add(self.tag)
        new_count = Item.objects.count()
        self.assertEqual(last_count, new_count)

    def test_data_base_catalogtag(self):
        last_count = Tag.objects.count()
        item = Tag(
            is_published=True,
            name="Tag-6",
            slug="This_Is_The_Tag-6",
        )
        item.full_clean()
        item.save()
        new_count = Tag.objects.count()
        self.assertEqual(last_count + 1, new_count)

        last_count = Tag.objects.count()
        with self.assertRaises(django_exceptions.ValidationError):
            item = Tag(
                is_published=True,
                name="6",
                slug="плохо работает",
            )
            item.full_clean()
            item.save()
        new_count = Tag.objects.count()
        self.assertEqual(last_count, new_count)

    def test_data_base_catalogcategory(self):
        last_count = Category.objects.count()
        item = Category(
            is_published=True,
            name="Tag-6",
            slug="This_Is_The_Tag-6",
            weight=150,
        )
        item.full_clean()
        item.save()
        new_count = Category.objects.count()
        self.assertEqual(last_count + 1, new_count)

        last_count = Category.objects.count()
        with self.assertRaises(django_exceptions.ValidationError):
            item = Category(
                is_published=True, name="6", slug="плохо работает", weight=150
            )
            item.full_clean()
            item.save()

            item = Category(
                is_published=True,
                name="6",
                slug="плохо работает",
                weight=32768,
            )
            item.full_clean()
            item.save()

            item = Category(
                is_published=True, name="6", slug="плохо работает", weight=-123
            )
            item.full_clean()
            item.save()
        new_count = Category.objects.count()
        self.assertEqual(last_count, new_count)

    def test_norm_name_for_category(self):
        item_positive = Category(
            is_published=True, name="Tag123", slug="slug", weight=100
        )
        item_positive.full_clean()
        item_positive.save()
        last_count = Category.objects.count()
        with self.assertRaises(django_exceptions.ValidationError):
            item_negative = Category(
                is_published=True,
                name="Tag!1,&23-",
                slug="slug123",
                weight=100,  # noqa
            )
            item_negative.full_clean()
            item_negative.save()
        new_count = Category.objects.count()
        self.assertEqual(last_count, new_count)

    def test_norm_name_tag(self):
        item_positive = Tag(
            is_published=True,
            name="Tag123",
            slug="slug",
        )
        item_positive.full_clean()
        item_positive.save()
        last_count = Tag.objects.count()
        with self.assertRaises(django_exceptions.ValidationError):
            item_negative = Tag(
                is_published=True,
                name="Tag!1,&23-",
                slug="slug123",
            )
            item_negative.full_clean()
            item_negative.save()
        new_count = Tag.objects.count()
        self.assertEqual(last_count, new_count)
