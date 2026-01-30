# We are creating this for multiple buildders

class Home():
    def __init__(self, size, location, total_house, builder_name):
        self.property_size = size
        self.location = location
        self.house_left = int(total_house)
        self.builder_name = builder_name

    def buy_house(self, customer_name):
        print("Congratulations ", customer_name, "You have secured a house of size ", self.property_size, "at location", self.location, "From Builder", self.builder_name)
        self.house_left -= 1 
        print("House Left: ", self.house_left)

builder_manager_1 = Home("2000sq.ft", "bengaluru", "2000", "brigade")
builder_manager_2 = Home("700sq.ft", "delhi", "2500", "Kalidas")
builder_manager_3 = Home("1400sq.ft", "mumbai", "1250", "Hiranandani")

builder_manager_1.buy_house("Monal")
print(builder_manager_1.house_left)

builder_manager_1.buy_house("Alekya")
print(builder_manager_1.house_left)

builder_manager_2.buy_house("Mohit")
print(builder_manager_2.house_left)

builder_manager_2.buy_house("Yusuf")
print(builder_manager_2.house_left)

builder_manager_3.buy_house("Rohit")
print(builder_manager_3.house_left)
