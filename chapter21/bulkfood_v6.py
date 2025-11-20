import model_v6 as model



@model.entity
class LineItem:
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()
    
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
        
    def subtotal(self):
        return self.weight * self.price
    
    
raisins = LineItem('Golden raisins', 10, 6.95)
print(dir(raisins)[:3])  # ['_NonBlank#description', '_Quantity#price', '_Quantity#weight']
print(LineItem.description.storage_name) # _NonBlank#description
print(raisins.description) # Golden raisins
print(getattr(raisins, '_NonBlank#description')) # Golden raisins
