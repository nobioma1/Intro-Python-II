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

  def get_room(self):
    return self.name
  
  def __str__(self):
    return f"Room Name: {self.name} \nRoom Description: {self.description}"