class Counter(object):
    def __init__(self, field_value = 0):
        self.field_value = field_value

    def add(self, number = 1):
        self.field_value += number
        return self.field_value