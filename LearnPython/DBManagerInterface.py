from abc import abstractmethod


class DBManagerInterface:

    @abstractmethod
    def __init__(self, table_name): raise NotImplementedError

    @abstractmethod
    def create_table(self): raise NotImplementedError

    @abstractmethod
    def drop_table(self): raise NotImplementedError
