class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}\t - {self.description}"

    def on_take(self):
        return f"You have picked up {self.name}"

    def on_drop(self):
        return f"You have dropped up {self.name}"

    def get_name(self):
        return self.name
