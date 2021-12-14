 
class Player:
    
    def __init__(self, name):
        self.name = name
        self.inventory = {}
        self.money = 0
        self.posX = 0
        self.posY = 0

    def __str__(self):
        return f"Player: {self.name}"

    def add_item(self, item, qty):
        ''' Adjusts players inventory, adds item if qty is positive and item does
            not currently exists in inventroy, adjusts quantity if item already exists
        '''
        if qty < 1:
            raise ValueError("Please use subtract_item() to remove item from Player Inventory")
        try:
            item.is_item() # Function should fail at this check
            if item.name.lower() in self.inventory:
                # If the item is already in the map tile 
                # Increase the Value of the Item's qty by qty
                self.inventory[item.name.lower()]["qty"] += qty
            else:
                self.inventory[item.name.lower()] = {
                    "item" : item,
                    "qty" : qty
                }

        except:
            raise ValueError("Item must be a tage Item() class or one of it's children")
    
    def remove_item(self, item):
        item = item.lower()
        try:
            if item.lower() in self.inventory:
                i = self.inventory[item.lower()]["item"]
                qty = self.inventory[item.lower()]["qty"]

                del self.inventory[item]

                return [i, qty]
            
            raise ValueError(f"Item {item} does not exist in the inventory")
        except:
            raise ValueError("Item name does not exist in Inventory")

    def check_item(self, item):
        if item.lower() in self.inventory:
            return True
        else:
            return False

    def has_inventory(self):
        return True

    def player_pos(self):

        return [self.posX, self.posY]