import re

class Email:
    def __init__(self, email: str):
        if not self.is_valid(email):
            raise ValueError("Invalid email format")
        self.value = email

    @staticmethod
    def is_valid(email: str) -> bool:
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def __str__(self):
        return self.value


class PhoneNumber:
    def __init__(self, phone_number: str):
        if not self.is_valid(phone_number):
            raise ValueError("Invalid phone number format")
        self.value = phone_number

    @staticmethod
    def is_valid(phone_number: str) -> bool:
        return re.match(r"^\+?[0-9]{7,15}$", phone_number) is not None

    def __str__(self):
        return self.value


class PostalCode:
    def __init__(self, postal_code: str):
        if not self.is_valid(postal_code):
            raise ValueError("Invalid postal code format")
        self.value = postal_code

    @staticmethod
    def is_valid(postal_code: str) -> bool:
        return re.match(r"^\d{4,6}$", postal_code) is not None  # Adjust regex for specific regions

    def __str__(self):
        return self.value
