import customer


class customerDTO:
    def __init__(self, customer):
        self.id = customer.get_id()
        self.name = customer.get_age()
        self.age = customer.get_age()
        self.weight = customer.get_weight()

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
