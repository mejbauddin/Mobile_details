class Mobile:
    def __init__(self,name, model, processor, ram, rom):
        self.name = name
        self.model = model
        self.processor = processor
        self.ram = ram
        self.rom = rom
    def show_details(self,price):
        self.price = price
        print(self.name)
        print("Model :", self.model)
        print("Processor :", self.processor)
        print("Ram :",self.ram)
        print("Rom :",self.rom)
        print("Price :", self.price)

realme = Mobile("Realme X", "3454x", "pentiam", "8GB", 128)
realme.show_details("$50")
iphone = Mobile("Iphone X", "54x", "pentiam", "12GB", 128)
iphone.show_details("$100")
