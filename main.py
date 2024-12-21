from transport import func
import json
from transport import Client
from transport import Vehicle
from transport import Train, Airplane, TransportCompany

def add_client(): #функция для вывода всех записей
    name = input("Введите имя клиента: ")
    vip = False
    cargo_weight = 0
    try:
        cargo_weight = int(input("Введите вес груза: "))
    except:
        print("Некорректное значение. Использовано значение по умолчанию")
    v = input("is vip?(y/n):").lower()
    if v=='y':
        vip = True
    elif v == "n":
        vip = False
    else:
        print("Некорректное значение. Использовано значение по умолчанию")
    info={'name':name, 'cargo_weight':cargo_weight, 'is_vip':vip}
    func.add_to_client_list(info)
    return Client.Client(name, cargo_weight, vip)

def add_transport(): #функция для вывода всех записей
    try:
        t = int(input("Введите вид транспорта\n1-поезд 2-самолёт\n"))
        if(t==1):  
            try:
                capacity = int(input("Введите грузоподъёмность: "))
                number_of_cars = int(input("Введите количество вагонов:"))
            except:
                print("Некорректное значение")
            func.add_to_transport_list(Train.Train.add_to_transport_list(Train.Train(capacity, number_of_cars)))
        elif(t==2):  
            try:
                capacity = int(input("Введите грузоподъёмность: "))
                number_of_cars = int(input("Введите максимальную высоту подъёма:"))
            except:
                print("Некорректное значение")
            func.add_to_transport_list(Airplane.Airplane.add_to_transport_list(Airplane.Airplane(capacity, number_of_cars)))
        else:
            print("Некорректное значение")
    except:
        print("Некорректное значение")
    

def menu(company): #функция "меню"
    c = int(input("=========\n1 - Добавить клиента \n2 - Добавить транспорт\n3 - Распределить грузы \n4 - Вывести список транспорта \n5 - Выход\n"))

    if c == 1: #добавляет клиента
        add_client()

    elif c == 2:#добавляет транспорт
        add_transport()
    
    elif c == 3: #добавляет транспортную компанию
        company.optimize_cargo_distribution()
        
    elif c == 4: #находится id в файле, после чего запись с нужным id удаляется
        with open("transport\\transport.json", "r", encoding="utf-8") as transport:
            data = json.load(transport)
        for vehicle in data:
            print(f"ID: {vehicle['id']}, Грузоподъемность: {vehicle['capacity']}, Загруженность: {vehicle['current_load']}")
    
    elif c == 5: #завершается цикл
        exit()
        
    else: #при вводе некорректного значения
        print('Введите корректное значение')

def main(): #главная функция #открывается файл json и записывается в data
    company_name = input("Введите название компании: ")
    company = TransportCompany.TransportCompany(company_name)
    while True: #цикл повторяется постоянно
        menu(company) #запускается функция "меню"

if __name__=="__main__":
    main()
