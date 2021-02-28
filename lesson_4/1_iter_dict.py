"""
    Сделать свою реализацию словаря, в котором будет переопределен метод __iter__,
    чтобы он возвращал итератор не по ключам, а сразу по паре ключ, значение.

    Используйте наследование от встроенного типа dict, и полиморфизм для метода __iter__.
    Конструктор базового класса переопределять не нужно.

    Чтобы получить пары ключ-значение используйте либо метод базового self.items() либо
    функцию zip() для self.keys() и self.values()
"""

from typing import Iterator, Tuple, Hashable, Any


class MyDict(dict):
    def __init__(self, dictionary):
        super().__init__(dictionary)

    def __iter__(self) -> Iterator[Tuple[Hashable, Any]]:
        items = list(zip(self.keys(), self.values()))
        while items:
            yield items.pop(0)


if __name__ == '__main__':
    d = MyDict({'a': '0', 'b': 1, 'c': 42})
    for i in d:
        print(i)
