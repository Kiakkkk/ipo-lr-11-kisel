class Client:#класс клиента
    
    def __init__(self, name:str, cargo_weight: int, is_vip: bool = False): 
        self.name = name#имя
        self.cargo_weight = cargo_weight#вес груза
        self.is_vip = is_vip#вип-статус
        

    