"""
Двусвязный список на основе односвязного списка.

    Самостоятельное задание. В двусвязном списке должны быть следующие методы:
    - **`__str__`**
    - **`__repr__`**
    - **`__getitem__`**
    - **`__setitem__`**
    - **`__len__`**
    - **`insert`**
    - **`index`**
    - **`remove`**
    - **`append`**
    - **`__iter__`**

    Необязательно все эти методы должны быть переопределены в явном виде. По максимуму используйте
    наследование, если поведение списков в контексте реализации указанных метод схоже.
    С точки зрения наследования по минимуму перегружайте методы. При необходимости рефакторите базовый класс,
    чтобы локализовать части кода во вспомогательные функции, которые имеют различное поведение
    в связном и двусвязном списках.
    Стремитесь к минимизации кода в дочернем классе.

    Есть какой-то метод класса DoubleLinkedList хотите отработать в явном виде ещё раз, не возбраняется.
"""

from typing import Any, Sequence, Optional


class LinkedList:
    class Node:
        """
        Класс, описывающий элементы "одного типа" (узлы),
        последовательно связанные между собой.
        """
        def __init__(self, value, next_=None):
            """
            Создаем новый узел для односвязного списка

            :param value: Любое значение, которое помещено в узел
            :param next_: следующий узел, если он есть
            """
            self.value = value
            self.next = next_

        @property
        def next(self):
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
            return f'{self.__class__.__name__}({self.value}, {self.next})'

        def __str__(self):
            return f'{self.value}'

    def __init__(self, data: Sequence = None):
        """
        Конструктор связанного списка
        :param data: последовательность, преобразуемая в связанный список
        """
        self.__len = 0
        self.head = None
        self.tail = None

        if data and self.is_iterable(data):
            for value in data:
                self.append(value)
        else:
            raise ValueError('Связанный список может быть создан только на основе непустого итерируемого объекта')

    def __repr__(self):
        """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
        return f"{type(self).__name__}({[value for value in self]})"

    def __str__(self):
        """Вызывается функциями str, print и format. Возвращает строковое представление объекта."""
        return f"{[value for value in self]}"

    def __len__(self) -> int:
        return self.__len

    def __step_by_step_on_nodes(self, index) -> Node:
        """Перемещение по узлам"""
        if not isinstance(index, int):
            raise TypeError('Индексы списка должны быть целыми числами')
        if index < 0:
            index += self.__len
        if not 0 <= index < self.__len:
            raise IndexError('Индекс списка вне допустимого диапазона')

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def __getitem__(self, item: int) -> Any:
        current_node = self.__step_by_step_on_nodes(item)
        return current_node.value

    def __setitem__(self, key: int, value: Any):
        current_node = self.__step_by_step_on_nodes(key)
        current_node.value = value

    def __iter__(self):
        self.generator = (self.__getitem__(current_index) for current_index in range(self.__len))
        return self.generator

    @staticmethod
    def _linked_nodes(left: Node, right: Optional[Node]):
        left.next = right

    def _make_node(self, value: Any,
                   next_: Optional['Node'] = None,
                   prev: Optional['Node'] = None):
        return self.Node(value, next_)

    def append(self, value: Any):
        """Добавление элемента в конец связного списка"""
        append_node = self._make_node(value)
        if self.head is None:
            self.head = append_node
            self.tail = append_node
        else:
            tail = self.tail
            self._linked_nodes(tail, append_node)
            self.tail = tail.next
        self.__len += 1

    def insert(self, index: int, value: Any) -> None:
        if not isinstance(index, int):
            raise TypeError('Индексы списка должны быть целыми числами')

        if index < 0:
            index += self.__len

        if index <= 0:
            insert_node = self._make_node(value)
            self._linked_nodes(insert_node, self.head)
            self.head = insert_node
            self.__len += 1
        elif 1 <= index <= self.__len-1:
            prev_node = self.__step_by_step_on_nodes(index-1)
            current_node = prev_node.next
            insert_node = self._make_node(value, next_=current_node, prev=prev_node)
            self._linked_nodes(prev_node, insert_node)
            self._linked_nodes(insert_node, current_node)
            self.__len += 1
        else:  # if index >= self.__len
            self.append(value)

    def index(self, value: Any) -> int:
        current_node = self.head
        current_index = 0

        while current_index <= self.__len-1:
            if current_node.value == value:
                return current_index
            current_node = current_node.next
            current_index += 1

        raise ValueError('Значение отсутствует в списке')

    def remove(self, value: Any) -> None:
        flag = True

        while self.head:
            if self.head.value == value:
                self.head = self.head.next
                self.__len -= 1
                flag *= 0
            else:
                break

        if self.head:
            prev_node = self.head
            current_node = self.head.next
            current_index = 1

            while current_index <= self.__len-1:
                if not current_node.next:
                    if current_node.value == value:
                        prev_node.next = None
                        self.tail = prev_node
                        self.__len -= 1
                        flag *= 0
                    break

                if current_node.value == value:
                    current_node = current_node.next
                    self._linked_nodes(prev_node, current_node)
                    self.__len -= 1
                    flag *= 0

                else:
                    prev_node = current_node
                    current_node = current_node.next
                    current_index += 1

        if flag:
            raise ValueError('Значение отсутствует в списке')

    def is_iterable(self, data) -> bool:
        """Метод для проверки является ли объект итерируемым"""
        return hasattr(data, '__iter__') and hasattr(self, '__iter__')


class DoubleLinkedList(LinkedList):
    class DoubleLinkedNode(LinkedList.Node):
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

    def __init__(self, data: Sequence = None):
        super().__init__(data)

    @staticmethod
    def _linked_nodes(left: DoubleLinkedNode, right: Optional[DoubleLinkedNode]):
        left.next = right
        right.prev = left

    def _make_node(self, value: Any,
                   next_: Optional['DoubleLinkedNode'] = None,
                   prev: Optional['DoubleLinkedNode'] = None):
        return self.DoubleLinkedNode(value, next_, prev)

    def __reversed__(self):
        self.current = self.tail
        while self.current:
            yield self.current.value
            self.current = self.current.prev


if __name__ == '__main__':
    dll = DoubleLinkedList([1, 2, 3])
    dll.insert(1, 3)
    print(dll)
    print(dll.index(3))
    dll.append(4)
    print(dll)
    print([i for i in reversed(dll)])
    dll.remove(3)
    print(dll)
