class Item:
    all = []
    def __init__(self,itemName,itemPrice) -> None:
        self.__itemName=itemName
        self.__itemPrice=itemPrice
        self.all.append(self)
    def __repr__(self) -> str:
        return f"Item({self.itemName},{self.itemPrice})"
        
item1 = Item("Bowl",100)
item2 = Item("Plate",150)
item1._Item__discount = 10
item1._Item__itemName = "Bowl Broken"
# print(item1._Item__itemName)
# print(item1.__discount)

print(item1.__dict__)