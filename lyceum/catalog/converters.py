class PositiveIntConverter:
    regex = r"[1-9]\d*"  # Регулярное выражение для целых чисел

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
