# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room
  
  def __str__(self):
    return f"Name: {self.name} \nCurrent Room: {self.current_room}"

  def get_current_room(self):
    return self.current_room
  
  def set_player_room(self, room):
    if room != None:
      self.current_room = room
    else:
      print("-->Sorry, you cannot move in this direction in your current room<--")