from abc import ABC, abstractmethod

class IFileSink(ABC):
    @classmethod
    @abstractmethod
    def sink(cls, data, filename):
        pass

class FileSink(IFileSink):
    @classmethod
    def sink(cls, data, filename):
        with open(f"{filename}", "w+") as file:
            file.write(data)
            file.close()
