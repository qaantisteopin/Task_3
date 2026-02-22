import random
import string
from dotenv import load_dotenv

load_dotenv()


class FakeUserGenerator:
    def generate_random_string(self, length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
    
    
    def generate_user_body(self):
        login = self.generate_random_string(10) + "@yandex.ru"
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)

        body = {
            "email": login,
            "password": password,
            "name": first_name
        }

        return body