"""
    1. Реализовать класс JsonFileDriver, который будет описывать логику считывания (записи) элементов из (в) json файл.
    2. Реализовать класс SimpleFileDriver, который будет описывать логику считывания (записи) элементов из (в) файл.
    3. В блоке __main__ протестировать работу драйверов
"""

import json
from typing import Sequence
from abc import ABC, abstractmethod


class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Sequence:
        """
        Считывает информацию из драйвера и возвращает её для объекта, использующего этот драйвер

        :return Последовательность элементов, считанная драйвером, для объекта
        """
        pass

    @abstractmethod
    def write(self, data: Sequence) -> None:
        """
        Получает информацию из объекта, использующего этот драйвер, и записывает её в драйвер

        :param data Последовательность элементов, полученная от объекта, для записи драйвером
        """
        pass


class JsonFileDriver(IStructureDriver):
    def __init__(self, filename_json: str):
        self.filename_json = filename_json

    def read(self) -> Sequence:
        with open(self.filename_json) as f:
            return json.load(f)

    def write(self, data: Sequence) -> None:
        with open(self.filename_json, 'w') as f:
            json.dump(data, f)


class SimpleFileDriver(IStructureDriver):
    def __init__(self, filename_txt: str):
        self.filename_txt = filename_txt

    def read(self) -> Sequence:
        with open(self.filename_txt) as f:
            return f.read().split(', ')

    def write(self, data: Sequence) -> None:
        with open(self.filename_txt, 'w') as f:
            f.write(', '.join([str(i) for i in data]))


if __name__ == '__main__':
    lst = [0, 1, 2, 3]
    SimpleFileDriver('test.txt').write(lst)
    lst1 = SimpleFileDriver('test.txt').read()
    print(lst1)
