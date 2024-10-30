class House:
    houses_history = []  # Атрибут класса для хранения названий объектов

    def __new__(cls, name, number_of_floors):
        instance = object.__new__(cls)  # Создаём новый объект
        cls.houses_history.append(name)  # Добавляем название объекта в историю
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print('Такого этажа нет')



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 15)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

# Снос последнего оставшегося объекта
del h1

print(House.houses_history)