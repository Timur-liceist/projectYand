from http import HTTPStatus

from django.conf import settings  # noqa
from django.test import TestCase


class ClassTestCaseMiddlewareReverseRusWords(TestCase):
    def test_reverse_rus_words_with_true_allow_reverse(self):
        global settings
        last_allow_reverse = settings.ALLOW_REVERSE
        settings.ALLOW_REVERSE = False
        settings.COUNT_OF_REQUESTS = 9
        response = self.client.get("/")
        self.assertEqual(response.content.decode(), "<body>Главная</body>")
        settings.ALLOW_REVERSE = last_allow_reverse

    def test_reverse_rus_words_with_false_allow_reverse(self):
        global settings
        last_allow_reverse = settings.ALLOW_REVERSE
        settings.ALLOW_REVERSE = True
        settings.COUNT_OF_REQUESTS = 9
        response = self.client.get("/")
        self.assertEqual(response.content.decode(), "<body>яанвалГ</body>")
        settings.ALLOW_REVERSE = last_allow_reverse


class ClassTestCaseHomepage(TestCase):
    def test_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


class ClassTestCaseCoffeeEndpoint(TestCase):
    def setUp(self):
        global settings
        settings.COUNT_OF_REQUESTS = 0

    def test_coffee_endpoint(self):
        response = self.client.get("/coffee/")
        self.assertEqual(response.status_code, HTTPStatus.IM_A_TEAPOT)
        self.assertEqual(response.content.decode(), "Я чайник")
