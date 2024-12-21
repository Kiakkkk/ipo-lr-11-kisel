from uuid import uuid4 #библиотека для id
from transport import Client

class err(Exception):
    def __init__(self):
        super().__init__("Произошла ошибка")

class Vehicle:
    def __init__(self, capacity:int): #функция добавляющая аргументы при создании экземпляра класса
        self.vehicle_id = str(uuid4()).split('-')[0]#id транспорта
        self.capacity = capacity#грузоподъёмность
        self.current_load = 0#загруженность
        self.clients_list = list()#список клиентов чьи грузы загружены

    def load_cargo(self, client:Client.Client):#функция загружающая груз на транспортное средство
        try:
            self.current_load += client.cargo_weight 
        except:
            raise err() 

    def __str__(self):#магический метод
        data = "ID: " + self.vehicle_id + "\nГрузоподъемность: " + str(self.capacity) + "\nТекущая загрузка: " + str(self.current_load)
        return data
