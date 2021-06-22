from abc import ABC, abstractmethod


class GameInterface(ABC):
    @abstractmethod
    def reset_game():
        pass

    @abstractmethod
    def get_table():
        pass

    @abstractmethod
    def get_row():
        pass

    @abstractmethod
    def get_column():
        pass

    @abstractmethod
    def get_rtl_diagonal():
        pass

    @abstractmethod
    def get_ltr_diagonal():
        pass


class PlayerInterface(ABC):
    @abstractmethod
    def mark():
        pass
