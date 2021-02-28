"""
Сделать DoubleLinkedNode наследуясь от класса Node

    1. В конструкторе DoubleLinkedNode обязательно вызвать конструктор базового класса и определить дополнительный
        атрибут self.prev, хранящий в себе ссылку на предыдущий узел. Тем самым дополняя функциональность базового класса,
        сохраняя его логику.
    2. Атрибут экземпляра prev сделать свойством prev. Определить для него getter и setter c проверками аналогичными
        свойству next в класса Node.
    3. В классе Node вынести проверку присваиваемого узла в setter свойства next во внутренний метод.
        Данный метод должен быть внутренним и не доступным пользователю.
    4. В классе DoubleLinkedNode воспользоваться методом из прошлого шага, чтобы проверить setter свойства prev.
        Каким должен быть этот метод?
            - protected
            - private
    5. Для DoubleLinkedNode перегрузить метод __repr__, метод __str__ оставить без изменений.
"""
from typing import Any, Optional


class Node:
    """
    Внутренний класс, класса LinkedList.

    Пользователь напрямую не работает с узлами списка, узлами оперирует список.
    """

    def __init__(self, value: Any, next_: Optional['Node'] = None, prev: Optional['Node'] = None):
        """
        Создаем новый узел для односвязного списка

        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_  # Вызывается сеттер

    @property
    def next(self):
        """Getter возвращает следующий узел связного списка"""
        return self.__next

    @next.setter
    def next(self, next_: Optional['Node']):
        """Setter проверяет и устанавливает следующий узел связного списка"""
        self._is_node(next_)
        self.__next = next_

    def _is_node(self, property_):
        if not isinstance(property_, self.__class__) and property_ is not None:
            msg = f"Устанавливаемое значение должно быть экземпляром класса {self.__class__.__name__} " \
                  f"или None, не {property_.__class__.__name__}"
            raise TypeError(msg)

    def __repr__(self):
        """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
        return f"Node({self.value}, next_={None})"

    def __str__(self):
        """Вызывается функциями str, print и format. Возвращает строковое представление объекта."""
        return f"{self.value}"


class DoubleLinkedNode(Node):
    def __init__(self, value: Any,
                 next_: Optional['DoubleLinkedNode'] = None,
                 prev: Optional['DoubleLinkedNode'] = None):
        super().__init__(value, next_)
        self.prev = prev

    @property
    def prev(self):
        """Getter возвращает следующий узел связного списка"""
        return self.__prev

    @prev.setter
    def prev(self, prev: Optional['DoubleLinkedNode']):
        """Setter проверяет и устанавливает следующий узел связного списка"""
        self._is_node(prev)
        self.__prev = prev

    def __repr__(self) -> str:
        """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
        return f'{self.__class__.__name__}({self.value}, next={self.next}, prev={self.prev})'


if __name__ == '__main__':
    first_node = DoubleLinkedNode(5)
    second_node = DoubleLinkedNode(10)

    print(repr(first_node))
    print(repr(second_node))

    head = first_node
    first_node.next = second_node
    second_node.prev = first_node

    print(repr(first_node.next))
    print(repr(second_node.prev))
