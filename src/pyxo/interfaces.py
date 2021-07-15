from abc import ABC, abstractmethod


class GameInterface(ABC):
    @abstractmethod
    def reset_game(self):
        ...

    @abstractmethod
    def table(self):
        ...

    @abstractmethod
    def get_row(self, index):
        ...

    @abstractmethod
    def get_column(self, index):
        ...

    @abstractmethod
    def get_rtl_diagonal(self):
        ...

    @abstractmethod
    def get_ltr_diagonal(self):
        ...

    @abstractmethod
    def set_point(self, point, value):
        ...


class PlayerInterface(ABC):
    @abstractmethod
    def game(self):
        ...

    @abstractmethod
    def mark(self, point):
        ...
