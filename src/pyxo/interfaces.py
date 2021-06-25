from abc import ABC, abstractmethod


class GameInterface(ABC):
    @abstractmethod
    def reset_game(self):
        pass

    @abstractmethod
    def table(self) -> list:
        pass

    @abstractmethod
    def get_row(self, index) -> list:
        pass

    @abstractmethod
    def get_column(self, index) -> list:
        pass

    @abstractmethod
    def get_rtl_diagonal(self) -> list:
        pass

    @abstractmethod
    def get_ltr_diagonal(self) -> list:
        pass

    @abstractmethod
    def set_point(self, point, value):
        pass


class PlayerInterface(ABC):
    @abstractmethod
    def game(self) -> GameInterface:
        pass

    @abstractmethod
    def mark(self, point):
        pass
