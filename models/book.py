class Book:
    def __init__(self, name, desc, img):
        self.name = name
        self.desc = desc
        self.img = img
    def __str__(self):
        return f"{self.name} - {self.desc} - {self.img}"
    