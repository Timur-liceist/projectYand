import re

from django.conf import settings  # noqa


class ReverseRussianWordsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        global settings
        settings.COUNT_OF_REQUESTS += 1
        response = self.get_response(request)
        if settings.COUNT_OF_REQUESTS == 10:
            if settings.ALLOW_REVERSE:
                response.content = self.reverse_russian_words(
                    response.content.decode("utf-8")
                )

                settings.COUNT_OF_REQUESTS = 0

        if settings.COUNT_OF_REQUESTS % 10 == 0:
            settings.COUNT_OF_REQUESTS %= 10

        return response

    def reverse_russian_words(self, content):
        def flip_word(match):
            word = match.group()
            return word[::-1]

        russian_word_pattern = r"[а-яА-Я]+"
        content = re.sub(russian_word_pattern, flip_word, content)
        return content
