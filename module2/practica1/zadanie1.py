import json



















class Address:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country
    
    def to_json(self):
        return json.dumps(self.__dict__)

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def to_json(self):
        return json.dumps(self.__dict__)
    
    # Создаем объекты Address
address_json = '{"street": "Дубровская", "city": "Волгоград", "country": "Россия"}'
address_data = json.loads(address_json)

address = Address(address_data['street'], address_data['city'], address_data['country'])

# Создаем объект Person, используя объект Address в качестве атрибута
person_json = '{"name": "Клавдия", "age": 22, "address": ' + address_json + '}'
person_data = json.loads(person_json)

person = Person(person_data['name'], person_data['age'], address)