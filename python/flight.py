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
    def availableSeats(self):
        return self.capacity - len(self.passengers)
  

vuelo = Flight(5)
pasajerosList = ["Juan", "Pedro", "Maria"]
for person in pasajerosList:
    vuelo.addPasssenger(person)
    print(f"El pasajero {person} ha sido añadido")

print(vuelo.passengers)
print(vuelo.capacity)
vuelo.addPasssenger("Ana")
