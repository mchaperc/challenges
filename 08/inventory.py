import sys

class Inventory(object):
    def __init__(self, name=""):
        self._name = name
        self._rooms = {}
        self.build_inventory()

    def get_name(self):
        return self._name

    def print_all_items_in_room(self, room="all"):
        if room == "all":
            for room in self._rooms:
                print "Contents of {}:".format(room)
                for item in self._rooms[room]:
                    print "    {} - ${}".format(item['item_name'], item['item_value'])
        else:
            print "Contents of {}:".format(room)
            for item in self._rooms[room]:
                print "    {} - ${}".format(item['item_name'], item['item_value'])

    def calculate_total_item_value_in_room(self, room="all"):
        total = 0
        if room == "all":
            for room in self._rooms:
                for item in self._rooms[room]:
                    total += int(item['item_value'])
        else:
            for item in self._rooms[room]:
                total += int(item['item_value'])
        print "${}".format(total)

    def build_inventory(self):
        user_choice = 0
        while user_choice != str(9):
            user_prompt = """
Please choose one of the following actions (type the number that corresponds to the action you'd like to perform):
    1) add a room
    2) add an item to a room
    3) print the contents of a room
    4) print the contents of entire inventory
    5) print the dollar value of the contents of a room
    6) print the dollar value of the contents of the entire inventory
    9) exit program
            """
            user_choice = raw_input(user_prompt)
            if user_choice != str(9):
                self.determine_action_from_user_input(user_choice)

    def determine_action_from_user_input(self, user_choice=str(9)):
        if user_choice == str(9):
            self.print_all_items_in_room(room="all")
            print "All done."
        elif user_choice == str(1):
            self.add_room()
        elif user_choice == str(2):
            self.add_item_to_room()
        elif user_choice == str(3):
            print "Room List:"
            for room in self._rooms:
                print "{}".format(room)
            room_to_print = raw_input("Which room's contents would you like to view?")
            self.print_all_items_in_room(room=room_to_print)
        elif user_choice == str(4):
            self.print_all_items_in_room(room="all")
        elif user_choice == str(5):
            print "Room List:"
            for room in self._rooms:
                print "{}".format(room)
            room_to_print = raw_input("Which room's contents would you like to tally?")
            self.calculate_total_item_value_in_room(room=room_to_print)
        elif user_choice == str(6):
            self.calculate_total_item_value_in_room(room="all")

    def add_room(self):
        room_name = ""
        while not len(room_name):
            room_name = raw_input("Please provide a name for the room you'd like to add.\n")
        if room_name in self._rooms:
            print "That room already exists!"
            return
        self._rooms[room_name] = []
        print "{} added to inventory! Now add some items to your new room.".format(room_name)
    
    def add_item_to_room(self):
        if not len(self._rooms):
            print "There are no rooms added yet! Try adding a room before adding items."
            return
        room_to_insert_item_into = ""

        while not len(room_to_insert_item_into):
            for room in self._rooms:
                print "    - {}".format(room)
            room_to_insert_item_into = raw_input("Please choose the room into which you'd like to insert an item: ")
            
            if room_to_insert_item_into not in self._rooms:
                print "That room hasn't been added yet."
                return
        
        item_name = ""
        while not len(item_name):
            item_name = raw_input("Please provide the name of the item you'd like to add: ")
            if item_name in self._rooms[room_to_insert_item_into]:
                print "That item already exists in this room. Try choosing a different name."
        
        item_value = ""
        while not len(item_value):
            item_value = raw_input("Please provide the value of {}: ".format(item_name))
        
        self._rooms[room_to_insert_item_into].append({"item_name": item_name, "item_value": item_value})
        print "{} successfully added to {}!".format(item_name, room_to_insert_item_into)
        


if __name__ == "__main__":
    inventory_name = raw_input("What would you like to call your inventory?\n\n")

    inventory = Inventory(name=inventory_name)
