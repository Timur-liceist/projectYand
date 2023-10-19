from django.test import TestCase


class ClassTestCaseAbout(TestCase):
    def test_description(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
