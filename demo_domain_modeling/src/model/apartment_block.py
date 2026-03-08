from dataclasses import dataclass

@dataclass
class ApartmentBlock:
    id: int
    name: str
    address: str
    number_of_floors: int
    units_per_floor: int