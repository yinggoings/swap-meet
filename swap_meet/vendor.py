class Vendor:
    def __init__(self,inventory=[]):
        self.inventory = inventory

    def add(self,item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_category(self,category):
        return [item for item in self.inventory if item.category == category]
    
    def swap_items(self,swap_vendor,my_item,their_item):
        if my_item not in self.inventory or their_item not in swap_vendor.inventory:
            return False
        self.inventory.remove(my_item)
        self.inventory.append(their_item)
        swap_vendor.inventory.remove(their_item)
        swap_vendor.inventory.append(my_item)
        return True