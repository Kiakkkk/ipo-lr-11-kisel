from transport import Vehicle

class Airplane(Vehicle.Vehicle):
    def __init__(self, capacity:int, max_altitude):
        self.max_altitude = max_altitude
        super().__init__(capacity)
        

    def add_to_transport_list(self):  # переопределяем метод для добавления информации о самолёте
        info = {
            'id': self.vehicle_id,
            'capacity': self.capacity,
            'current_load': self.current_load,
            'client_list': self.clients_list,
            'max_altitude': self.max_altitude  # добавляем max_altitude в info
        }
        return info
    def __str__(self):
        return super().__str__()+"\nМаксимальная высота полёта: "+str(self.max_altitude)