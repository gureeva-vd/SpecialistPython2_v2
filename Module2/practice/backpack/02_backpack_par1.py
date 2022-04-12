class Item:
    def __init__(self, n, w, c):
        self.name = n  # Название предмета
        self.weight = w  # Вес предмета, в килограммах
        self.cost = c  # Цена предмета, пусть будет, в рублях

    def show(self):
        return f'{self.name} вес: {self.weight} цена: {self.cost}'

class BackPack:  # рюкзак
    def __init__(self):
        self.items = []  # Предметы, которые хранятся в рюкзаке

    def add_item(self, item: Item):
        self.items.append(item)
        # TODO: реализуйте метод

    def show_items(self):
        i = 1
        for item in self.items:
            print(i, item.show())
            i += 1
            
        # TODO: реализуйте метод


# Создаем предметы
item1 = Item("Гиря", 25, 500)
item2 = Item("Арбуз", 4, 300)

# Создаем пустой рюкзак
backpack = BackPack()

# Добавляем пару предметов в рюкзак
backpack.add_item(item1)
backpack.add_item(item2)

# Выводим все предметы в рюкзаке
backpack.show_items()
