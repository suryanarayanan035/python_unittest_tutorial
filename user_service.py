import requests
from converter import TextToListConverter, ListToCSVConverter 
from sink import FileSink
from custom_errors import RequestError
class UserService:
    @classmethod
    def pull_all_users(cls):
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        if response.ok:
            return response.text
        else:
            raise RequestError("Request is not successful.")


    @classmethod
    def save_users_to_file(cls, file_name, file_type):
        pulled_in_users = cls.pull_all_users()
        if file_type == 'csv':
            pulled_in_users = TextToListConverter.convert(pulled_in_users)
            pulled_in_users = ListToCSVConverter.convert(pulled_in_users, ['id', 'name', 'username', 'phone', 'email'])
        FileSink.sink(pulled_in_users, file_name)


