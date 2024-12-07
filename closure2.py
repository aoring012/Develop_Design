class DataClass(object):
    def __init__(self, checked_value):
        self.data = []
        self.checked_value = checked_value

    def add_data(self, check_value):
        if self.checked_value > check_value:
            self.data.append(check_value)

    def get_data(self):
        return self.data
