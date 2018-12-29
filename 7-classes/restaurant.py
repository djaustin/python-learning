class Restaurant():

    def __init__(self, restuarant_name, cuisine):
        self.restuarant_name = restuarant_name
        self.cuisine = cuisine

    def describe(self):
        print(f"{self.restuarant_name} serves {self.cuisine}")

    def open(self):
        print(f"{self.restuarant_name.capitalize()} is now open for business!")

r1 = Restaurant('Five Guys', 'burgers')

print(r1.restuarant_name)
print(r1.cuisine)
r1.describe()
r1.open()
