class customer:
    def __init__(self, id="", name="", age="", weight="", profile_pic_url=""):
        self.id = id
        self.name = name
        self.age = age
        self.weight = weight
        self.profile_pic_url = profile_pic_url

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_weight(self):
        return self.weight

    def get_profile_pic_url(self):
        return self.profile_pic_url

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_weight(self, weight):
        self.weight = weight

    def set_profile_pic_url(self, profile_pic_url):
        self.profile_pic_url = profile_pic_url
