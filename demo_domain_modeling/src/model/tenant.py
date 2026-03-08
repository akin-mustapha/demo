from .person import Person

class Tenant(Person):
  def __init__(self, id: int, first_name: str, last_name: str, email: str, phone_number: str, date_of_birth: str, tenant_id: str, apartment_number: str, lease_start_date: str, lease_end_date: str):
    super().__init__(id, first_name, last_name, email, phone_number, date_of_birth)
    self.tenant_id = tenant_id
    self.apartment_number = apartment_number
    self.lease_start_date = lease_start_date
    self.lease_end_date = lease_end_date