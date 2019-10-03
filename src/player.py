# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room
        self.inventory = []
  
  def __str__(self):
        return f"\tName: {self.name} \tCurrent Room: {self.current_room}"

  def get_current_room(self):
    return self.current_room
  
  def set_player_room(self, room):
      self.current_room = room

    def move_player(self, room):
        if room != None:
            self.set_player_room(room)
    else:
      print("-->Sorry, you cannot move in this direction in your current room<--")

    def view_inventory(self):
        inventories = "Your Inventory:\n"
        if len(self.inventory) == 0:
            inventories += " There is no item in your inventory"
        else:
            for index, item in enumerate(self.inventory):
                inventories += f" {index + 1}. {item}\n"
        return inventories

    def add_inventory(self, item):
        self.inventory.append(item)

    def remove_inventory_item(self, item_index):
        self.inventory.pop(item_index)
