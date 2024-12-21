from transport import Client, Vehicle 

class TransportCompany:

    def __init__(self, name:str):
        self.name = name
        self.clients = ()
        self.vehicles = ()
        
    def add_vehicle(self, vehicle):
        if(type(vehicle)==Vehicle.Vehicle):
            self.vehicles.append(vehicle)
            self.vehicles.sort(key=lambda vehicle: vehicle.capacity, reverse=True)
            print("Добавлено транспортное средство: ", vehicle.vehicle_id)
        else:
            print("Произошла ошибка")

    def list_vehicles(self):
        return self.vehicles
    
    def add_client(self,client):
        if(type(client)==Client.Client):
            self.clients.append(client)
            self.clients.sort(key=lambda client: client.is_vip, reverse=True)
            print("Добавлен клиент")
        else:
            print("Произошла ошибка")

    def optimize_cargo_distribution(self):
        for vehicle in self.vehicles:
            for client in self.clients:
                if vehicle.current_load + client.cargo_weight <= vehicle.capacity:
                    vehicle.load_cargo(client)
                    vehicle.clients_list.append(client)
                    print(f"Груз клиента {client.name} загружен на транспортное средство {vehicle.vehicle_id}")
                    self.clients.remove(client)  # Убираем клиента из списка
                    break
            if not self.clients:
                break
        
        if self.clients:
            print("Не все грузы удалось распределить, не хватает транспорта.")
        else:
            print("Все грузы успешно распределены по транспортным средствам.")



