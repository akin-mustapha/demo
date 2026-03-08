from dataclasses import dataclass

@dataclass
class Apartment:
    id: int
    block_id: int
    floor_number: int
    unit_number: str
    number_of_bedrooms: int
    number_of_bathrooms: int
    square_feet: float