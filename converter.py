from abc import ABC, abstractmethod

class DataConverter(ABC):
    @classmethod
    @abstractmethod
    def convert(cls, input_content, keys=None):
        pass

class TextToListConverter(DataConverter):
    """
        This class converts parses given text to a list of dictionaries.
        The input text should be in json format.
    """
    @classmethod
    def convert(cls, input_content, keys=None):
        import json
        return json.loads(input_content)

class ListToCSVConverter(DataConverter):
    """
        This class converts given list of dictionries to CSV.
    """
    @classmethod
    def convert(cls, input_content, keys=None):
        if not keys:
            raise ValueError("Please provide keys to include in csv as columns")
        csv_data =",".join([key for key in keys]) + "\n"
        if not isinstance(input_content, list):
            raise TypeError("Please provide a list as input")
        for obj in input_content:
            csv_data += ",".join([str(obj[key]) for key in keys])+ "\n"
        return csv_data

