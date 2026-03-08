from .person import Person

class Employee(Person):
  def __init__(self, id: int, first_name: str, last_name: str, email: str, phone_number: str, date_of_birth: str, employee_id: str, position: str, salary: float):
    super().__init__(id, first_name, last_name, email, phone_number, date_of_birth)
    self.employee_id = employee_id
    self.position = position
    self.salary = salary