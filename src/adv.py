from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [
                         Item("spoon", "Use to take soup"),
                         Item("clock", "Know the time at the moment, time is money")
                     ]),

    'foyer':    Room("Foyer",
                     "Dim light filters in from the south. Dusty passages run north and east.",
                     [
                         Item("book", "Write your experience"),
                         Item("mask", "For the dusty air in the passage"),
                         Item("blanket", "For the cold nights")
                     ]),

    'overlook': Room("Grand Overlook",
                     """A steep cliff appears before you, falling
                    into the darkness. Ahead to the north, a light flickers in
                    the distance, but there is no way across the chasm.
                    """,
                     [Item("lamp", "When the light flickers")]),

    'narrow':   Room("Narrow Passage",
                     """The narrow passage bends here from west
                    to north. The smell of gold permeates the air.""",
                     [Item("bag", "Carry you items")]),

    'treasure': Room("Treasure Chamber",
                     """You've found the long-lost treasure
                    chamber! Sadly, it has already been completely emptied by
                    earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Main


# Make a new player object that is currently in the 'outside' room.

player = Player('Lupita', room['outside'])

# Write a loop that:

while True:
    print("\n\t**Command LineAdventure Room Game**")

    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).

    player_current_room = player.get_current_room()
    print(f"\nCurrent Room:\n{player_current_room}")

    # * Print Current room Items

    current_room_items = player_current_room.view_room_items()
    print(current_room_items)

    # * Waits for user input and decides what to do.

    user_input = input(
        """What do you want to do now? 
        (n - North, s - South, e - East, w - West, i - Your Inventory, q - Quit)
        (take <ITEM_NAME> - Pick Item, drop <ITEM_NAME> - Drop Item )
    > """).lower()

    # If the user enters a cardinal direction, attempt to move to the room there.

    if user_input == "n":
        next_room = player_current_room.n_to
        player.move_player(next_room)
    elif user_input == "s":
        next_room = player_current_room.s_to
        player.move_player(next_room)
    elif user_input == "e":
        next_room = player_current_room.e_to
        player.move_player(next_room)
    elif user_input == "w":
        next_room = player_current_room.w_to
        player.move_player(next_room)
    elif user_input == "i":
        inventories = player.view_inventory()
        print(inventories)
    elif 'drop' in user_input:
        print(player.drop_item(user_input))
    elif 'take' in user_input:
        print(player.take_item(user_input))
    elif user_input == "q":

        # If the user enters "q", quit the game.

        print("Bye! See you Later")
        break
    else:

        # Print an error message if the movement isn't allowed.

        print(f"-->Movement {user_input} is not allowed<--\n")
