class Inventory:
    def __init__(self, __capacity: int):
        self.__capacity = __capacity
        self.items = []

    def add_item(self, item: str):
        if self.__capacity > 0:
            self.__capacity -= 1
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return len(self.items)

    def __repr__(self):
        items = ', '.join(self.items)
        return f'Items: {items}.\nCapacity left: {self.__capacity}'
