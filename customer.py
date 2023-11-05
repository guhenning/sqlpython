class customer:
    def __init__(self, name="", age="", weight="", id=""):
        self.id = id
        self.name = name
        self.age = age
        self.weight = weight

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_weight(self):
        return self.weight

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_weight(self, weight):
        self.weight = weight
