"""
Реализовать класс LinkedListWithDriver от класса LinkedList.
Дочерний класс должен уметь работать с реализованными ранее драйверами.

    1. Реализовать свойство driver, которое будет возвращать используемый драйвер и проверять, что устанавливаемый
        драйвер является экземпляром класса IStructureDriver.
    2. Реализовать метод read, который с помощью встроенного драйвера будет получать последовательность элементов и
        помещать их в самого себя. При вызове метода связанный список должен полностью перезаписываться новыми элементами.
    3. Реализовать метод write, который передавать последовательность элементов для записи драйвером.
    4. Протестировать паттерн "Стратегия" в ключе независимости работы экземляров LinkedListWithDriver от драйверов
        IStructureDriver. LinkedListWithDriver должен уметь работать со всеми экземплярами дочерних классов класс IStructureDriver.
    5. LinkedListWithDriver должен поддерживать "горячую замену" драйвера, то есть без удаления и создания нового
        экземпляра LinkedListWithDriver, а замена драйвера существующего экземпляра.
"""

from lesson_5.a_linkedlist import LinkedList
from lesson_5.a_driver import IStructureDriver, JsonFileDriver


class LinkedListWithDriver(LinkedList):
    def __init__(self, data, driver: IStructureDriver = None):
        super().__init__(data)
        self.driver = driver

    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, driver):
        if not isinstance(driver, IStructureDriver):
            raise TypeError('Используемый объект не является драйвером')
        self.__driver = driver

    def read(self):
        """Взять драйвер и считать из него информацию в LinkedList"""
        self.clear()
        for item in self.__driver.read():
            self.append(item)
        return self

    def write(self):
        """Взять драйвер и записать в него информацию из LinkedList"""
        self.__driver.write([i for i in self.__iter__()])


if __name__ == '__main__':
    json_driver = JsonFileDriver('test.json')
    ll = LinkedListWithDriver([1, 2, 3, 4, 5], json_driver)
    ll.write()
    ll1 = LinkedListWithDriver(data=[], driver=json_driver).read()
    print(ll1)
