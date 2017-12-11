class Station(object):
    def __init__(self, gas_amount = 10000):
        self.gas_amount = gas_amount

    def refill(self, car):
        self.gas_amount -= car.capacity
        car.gas_amount += car.capacity

class Car(object):
    def __init__(self, gas_amount = 0, capacity = 100):
        self.gas_amount = gas_amount
        self.capacity = capacity

car = Car()
station = Station()
station.refill(car)
print("Car gas amount: ", car.gas_amount)
print("Station gas amount: ", station.gas_amount)
print("Car capacity: ", car.capacity)





