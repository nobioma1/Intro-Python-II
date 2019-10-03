# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, room_items=[]):
    self.name = name
    self.description = description
        self.room_items = room_items
    self.n_to = None  
    self.s_to = None
    self.e_to = None
    self.w_to = None 

    def __str__(self):
        return f" Room Name: {self.name}\n Room Description: {self.description}"

    def view_room_items(self):
        items = "Room Items:\n"
        if len(self.room_items) == 0:
            items += " There is no item in this room"
        else:
            for index, item in enumerate(self.room_items):
                items += f" {index + 1}. {item}\n"
        return items
    return self.name
  
  def __str__(self):
    return f"Room Name: {self.name} \nRoom Description: {self.description}"