import random
import string

def generate_user_data():
    username = ''.join(random.choices(string.ascii_lowercase, k=8))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return {
        "username": username,
        "password": password
    }
