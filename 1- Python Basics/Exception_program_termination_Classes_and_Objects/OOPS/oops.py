# We are builders and we are selling home at abc-123-werr-234

class Home():
    def __init__(self):
        self.property_size = "1200sqft"
        self.location = "abc-123-werr-234"
        self.house_left = 100

    def buy_house(self, customer_name):
        print("Congratulations ", customer_name, "You have secured a house of size ", self.property_size, "at location", self.location)
        self.house_left -= 1 
        print("House Left: ", self.house_left)

builder_manager = Home()
builder_manager.buy_house("Monal")
builder_manager.buy_house("Alekya")
builder_manager.buy_house("Mohit")
builder_manager.buy_house("Yusuf")
builder_manager.buy_house("Rohit")
