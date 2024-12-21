from transport import Vehicle

class Train(Vehicle.Vehicle):
    def __init__(self, capacity:int, number_of_cars:int):
        self.number_of_cars = number_of_cars
        super().__init__(capacity)

    def add_to_transport_list(self):  # переопределяем метод для добавления информации о поезде
        info = {
            'id': self.vehicle_id,
            'capacity': self.capacity,
            'current_load': self.current_load,
            'client_list': self.clients_list,
            'number_of_cars': self.number_of_cars  # добавляем number_of_cars в info
        }
        return info

        
    def __str__(self):
        return super().__str__()+"\nКоличество вагонов: "+str(self.number_of_cars)