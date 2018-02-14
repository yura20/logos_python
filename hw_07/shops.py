class Stuff:
    name = None
    price = None
    availability = None
    numerosity = None
    def __init__(self, name, price, availability, numerosity, **kwargs):
        self.name = name
        self.price = price
        self.availability = availability
        for key in kwargs:
            self.key = kwargs[key]
class Manager:
    name = None
    surname = None
    address = None
    contacts = None
    birth_date = None
    def __init__(self, name, surname, address, contacts, birth_date):
        self.name = name
        self.surname = surname
        self.address = address
        self.contacts = contacts
        self.birth_date = birth_date
class Store:
    manager = None
    contacts = None
    address = None
    name = None
    stuff = None
    def __init__(self, contacts, address, name):
        self.contacts = contacts
        self.address = address
        self.name = name
        self.stuff = []
    def add_stuff(self, name, price, **kwargs):
        self.stuff.append(Stuff(name, price, **kwargs))
    def get_availability_stuff(self):
        arr = []
        i = 0
        while i < len(self.stuff):
            if self.stuff[i].availability == True:
                arr.append(self.stuff[i].name)
            i+=1
        return arr
    def add_manager(self, name, surname, address, contacts, birth_date):
        self.manager = Manager(name, surname, address, contacts, birth_date)
    def get_managers_contacts(self):
        return [self.manager.name, self.manager.surname, self.manager.contacts]
    def change_price(self, stuff_index, percent):
        print(self.stuff[stuff_index].name)
        print("old price - ", self.stuff[stuff_index].price)
        self.stuff[stuff_index].price = (self.stuff[stuff_index].price * percent)/100 + self.stuff[stuff_index].price
        print("new price - ", self.stuff[stuff_index].price)
            
            
appleStore = Store("380557273904", "вул.Замарстинівська 8", "Apple Store")
appleStore.add_manager("Андрій", "Притула", "вул.Наукова 60/20", "380678456394", "20.12.1988")
appleStore.add_stuff(
    name = "iPhone 7",
    price = 9000,
    availability = False,
    numerosity = 7,
    capacity = "64GB",
    chip = "a9",
    baterry = "2700ma"
)
appleStore.add_stuff(
    name = "iPhone X",
    price = 19000,
    availability = True,
    numerosity = 10,
    capacity = "256GB",
    chip = "a11",
    camera = "12MP wide-angle and telephoto cameras",
    sensors = ["Face ID", "Barometer", "Three-axis gyro", "Accelerometer", "Proximity sensor", "Ambient light sensor"],
    baterry = "3000ma"
)
appleStore.add_stuff(
    name = "iMac Pro 2015",
    price = 90000,
    availability = True,
    numerosity = 2,
    display = "21.5, 4k Retina",
    processor = "3.4GHz quad-core Intel Core i5 (Turbo Boost up to 3.8GHz)",
    baterry = "12000ma",
    memory = "16GB of 2400MHz DDR4 memory",
    storage = "1TB SSD",
    graphics = "Radeon Pro 560 with 4GB of VRAM"
)

print("Доступний товар -", appleStore.get_availability_stuff())
print("Контакти менеджера -", appleStore.get_managers_contacts())
appleStore.change_price(1, -15)
appleStore.change_price(2, 5)
print("----------")

brain = Store("38056773975", "прос.Шевченка 3", "Brain")
brain.add_manager("Олег", "Шпак", "вул.Шевченка 123/12", "380546565365", "10.02.1990")
brain.add_stuff(
    name = "Lenovo S820",
    price = 2300,
    availability = True,
    numerosity = 8,
    display = "4.7 FullHd",
    capacity = "32GB",
    baterry = "2300ma",
    memory = "2GB"
)
print("Доступний товар -", brain.get_availability_stuff())
print("Контакти менеджера -", brain.get_managers_contacts())
brain.change_price(0, -5)








