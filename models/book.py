class Book:
    def __init__(self, name, img, desc):
        self.name = name
        self.img = img
        self.desc = desc
    def __str__(self):
        return f"{self.name} - {self.img} - {self.desc}"
    