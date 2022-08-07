# point class
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def addPasssenger(self, name):
        if self.openSeats():
           self.passengers.append(name)
        else:
            print("No seats available")
    def openSeats(self):
        if len(self.passengers) < self.capacity:
            return True 
  

vuelo = Flight(3)
vuelo.passengers = ["Juan", "Pedro"]
print(vuelo.passengers)
print(vuelo.capacity)
vuelo.addPasssenger("Ana")
print(vuelo.passengers)