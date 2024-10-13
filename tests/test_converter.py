import unittest

from unit_testing.converter import TextToListConverter, ListToCSVConverter
class TestTextToListConverter(unittest.TestCase):
    def test_convert(self):
        converted_data = TextToListConverter.convert('[{"key": "value"}]')
        self.assertIsInstance(converted_data, list)

class TestListToCSVConverter(unittest.TestCase):
    def test_convert(self):
        converted_data = ListToCSVConverter.convert([{"id": 1, "name":"test", "email": "test@mail.com"}], keys=["id", "name", "email"])
        csv_data = "id,name,email\n1,test,test@mail.com\n"
        self.assertEqual(converted_data, csv_data)

    def test_convert_raises_exception_if_keys_is_absent(self):
        """
            Test if exception is raised if keys is not passed to convert method.
        """
        with self.assertRaises(ValueError) as exception_context:
            ListToCSVConverter.convert([{"id": 1, "name":"test", "email": "test@mail.com"}])
        self.assertEqual(str(exception_context.exception), 'Please provide keys to include in csv as columns')
    def test_convert_raises_exception_if_input_data_is_not_list(self):
        """
            Test if exception is raised if keys is not passed to convert method.
        """
        with self.assertRaises(TypeError) as exception_context:
            ListToCSVConverter.convert(None, keys=["key"])
        self.assertEqual(str(exception_context.exception), 'Please provide a list as input')

