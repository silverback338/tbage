 # Class for MapTiles

class GameMap():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Map: {}".format(self.name)


class MapTile():
    # Base MapTile Class - Defines the minimum items necessary to create a map tile and the minimum functions needed for them
    def __init__(self, name):
        self.name = name
        self.shortDescription = ""
        self.intro = ""
        self.tile_inspect = {}
        self.map_items = {}

    def intro_text(self):
        raise NotImplementedError("Create a subclass of MapTile")

    def __str__(self):
        return "Tile: {}\nDescription:{}".format(self.name, self.shortDescription)
    
    def inspect_list(self):
        if len(self.tile_inspect) > 0:
            return True
        else:
            return False
    
    def add_item(self, item, qty):
        if qty < 1:
            raise ValueError("Please use subtract_item() to remove item from MapTile")
        try:
            item.is_item() # Function should fail at this check
            if item.name.lower() in self.map_items:
                # If the item is already in the map tile
                # Increase the Value of the item's qty by qty
                self.map_items[item.name.lower()]["qty"] += qty
            else:
                self.map_items[item.name.lower()] = {
                    "item" : item,
                    "qty" : qty
                }

        except:
            raise ValueError("Item must be a tage Item() class or one of it's children")

    def remove_item(self, item):
        item = item.lower()
        try:
            if item.lower() in self.map_items:
                # If item exists in the list, check to see if there is enough qty to complete transaction
                i = self.map_items[item.lower()]["item"]
                qty = self.map_items[item.lower()]["qty"]

                del self.map_items[item]

                return [i, qty]
            raise ValueError(f"Item {item} does not exist on current map tile")
        except:
            raise ValueError("Item name does not exist in MapTile")


    def check_item(self, item):
        if item.lower() in self.map_items:
            return True
        else:
            return False


    def has_inventory(self):
        return True


    def tile_items(self):
        return self.map_items



class StartTile(MapTile):
    
    def intro_text(self):
        return self.intro

    def short_description(self):
        return self.shortDescription


# Need to have subclasses of Map tiles
# - StartTile - will be the starting tile on a map
# - TransportTile - Will be a linking tile between 2 maps. 
# - GameTile - Will be a typical game play tiles