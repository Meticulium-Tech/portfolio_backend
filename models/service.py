class Service:
    def __init__(self, name, desc, icon):
        self.name = name
        self.desc = desc
        self.icon = icon
    def __str__(self):
        return f"{self.name} - {self.desc} - {self.icon}"
        