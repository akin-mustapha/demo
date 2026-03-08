from dataclasses import dataclass

@dataclass
class Person:
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    date_of_birth: str # Format: YYYY-MM-DD