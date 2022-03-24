class Magazine():
    def __init__(self, title, date, author, code, preview):
        self.title = title
        self.date = date
        self.author = author
        self.code = code
        self.preview = preview

    def __str__(self):
        return f"{self.title} {self.issue} {self.price}"