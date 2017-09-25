class Counter(object):
    def __init__(self, value = 0):
        self.value = value
        self.field_value = self.value

    def add(self, number = 1):
        self.field_value += number
        return self.field_value

    def get(self):
        return self.field_value

    def reset(self):
        self.field_value = self.value
        return self.field_value