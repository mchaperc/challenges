# Add room
# Add item to room
# Add value to item
# edit room
# edit item
# edit item value
# delete item
# delete room
# get room
# get item
# get rooms item appears in
# get items by value
# get all items for room
# get all items in inventory
# get number of items
# get number of rooms
# validate number of items in room (must meet minimum criteria)
# get dollar value of each room
# get dollar value of whole inventory
# get most/least expensive item per room
# get most/least expensive item in inventory


class Inventory():
    def __init__(self, name="", min_num_items_per_room=5):
        self._name = name
        self._items_per_room = min_num_items_per_room
        self._rooms = {}

    def add_room(self, room_name):
        if room_name not in self._rooms:
            self._rooms[room_name] = {}
        else:
            print("Sorry, that room already exists. Please try adding another.")

    def add_item(self, item_name=0, item_value=0, room_name=""):
        if room_name not in self._rooms:
            print("Sorry, but that room doesn't exist. You should try adding a room before supplying its contents.")
        else:
            if not item_name or item_value:
                print("Sorry, but you must supply both an item name and its value for it to be included in the inventory.")
            else:
                self._rooms[room_name][item_name] = item_value
    
    def get_room_items(self, room_name=""):
        if room_name not in self._rooms:
            print("Sorry, but that room doesn't exist. You should add a room before viewing its contents.")
        elif not len(self._rooms[room_name]):
            print("Sorry, but there are no items currently in the room you've requested to view. Please try adding some items to the room in question before viewing the room's inventory.")
        else:
            room_items = self._rooms[room_name]
            for item in room_items:
                print(f"{item} - ${room_items[item]}")

    def determine_which_method_user_chose(self, user_input=0):
        if not user_input or user_input > 17 or user_input < 1:
            print("Sorry, but I don't recognize that command")
        else:
            


options = {
    1: "1) Add a room",
    2: "2) Add an item to a room",
    3: "3) Edit a room",
    4: "4) Edit an item",
    5: "5) Get the contents of a room",
    6: "6) Get all of the contents of the house",
    7: "7) Get the most valuable item in a room",
    8: "8) Get the most valuable item in the whole house",
    9: "9) Delete a room",
    10: "10) Delete an item from a room",
    11: "11) Get the total dollar value of the items in a selected room",
    12: "12) Get the total dollar value of the items in the whole house",
    13: "13) Get the most expensive item in a room",
    14: "14) Get the least expensive item in a room",
    15: "15) Get the most expensive item in the whole house",
    15: "15) Get the least expensive item in the whole house",
    16: "16) Save house"
}

options_map = {
    1: 
}


if __name__ == "__main__":

    