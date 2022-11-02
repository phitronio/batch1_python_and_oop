import json


class Item:
    all=[]
    def __init__(self,name,price) -> None:
        self.name=name
        self.price=price
        self.all.append(self)
    @staticmethod
    def initialize():
        with open('extract.txt','r') as f:
            data = f.read()
            js = json.loads(data)
        for item in js:
            Item(
                name=item["name"],
                price=item.get("price")
            )
    def __repr__(self) -> str:
        return f"Item({self.name},{self.price})"
            
Item.initialize()
print(Item.all)