class RetailItem:
    def __init__(self, Description, Units_In_Inventory, Price):
        self.Description = Description
        self.Units_In_Inventory = Units_In_Inventory
        self.Price = Price

    def GetItem(self):
        print("Item's description: " + self.Description)
        print("Units in Inventory: " + str(self.Units_In_Inventory))
        print("Item price: " + str(self.Price) + "\n")


item1 = RetailItem("Jacket",12,59.95)
item2 = RetailItem("Designer Jeans",40,34.95)
item3 = RetailItem("Shirt",20,24.95)

item1.GetItem()
item2.GetItem()
item3.GetItem()