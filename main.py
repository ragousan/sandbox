import csv


class Item:
    pay_rate: float = 0.8 # The pay rater after 20% discount
    all: list = []
    def __init__(self, name: str, price: float, quantity: int = 0)-> None:
        # Run validations
        assert price >= 0, f"Price {price} not greater than zero"
        assert quantity >=0, f"Quantity {quantity} not greater than zero"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return (self.price * self.quantity)
    
    def apply_discount(self):    
        self.price *= self.pay_rate # Item.pay_rate cannot be overriden by instance (item2.pay_rate = 0.7)
        # pass
    
    def __repr__(self) -> str:
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"
        pass
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for element in items:
            # print(element)
            Item(
                name = element.get('name'),
                price = float(element.get('price')),
                quantity = float(element.get('quantity'))
            )
    @staticmethod
    def is_integer(num):
        # Count out .0 floats
        if isinstance():
            pass
        
        

          
print(Item.all)

Item.instantiate_from_csv()

print(Item.all)
# item1 = Item("Phone", 100, 2)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print("\n\n",Item.__dict__,"\n")
# print(item1.__dict__,"\n")

# for instan in Item.all:
#     print(instan.name,"\t",instan.price)

# print(Item.all)
# print(Item.all[0])
