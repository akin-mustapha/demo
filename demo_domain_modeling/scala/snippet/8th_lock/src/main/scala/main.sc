/*
  apartment model

  Entities
  - Apartment_block (number_of_apartments, map(apartment_no -> (Apartment, floor_number))
  - Apartment (no_rooms, kitchen_flag, living_room_flag, room_size -> map(room_name: size), blacony_flag)
  - People (first_name, last_name, age,)
    - Tenant (apartment_number, )
    - Manager (employee_number, role)
    - Security (employee_number, role)
    - Concierge (employee_number, role)
    
  Apartment 
  -  TwoBed
  -  OneBed

  
*/
case class Apartment_block(apartments: Map[String, List[Apartment]])

class Apartment(
    var no_rooms: Int
  , var kitchen_flag: Boolean
  , var living_room_flag: Boolean
  , var room_size: Map[String, Int]
  )


case class Person(first_name: String, last_name: String, age: Int)

class Tenant(first_name: String, last_name: String, age: Int, var apartment_no: Int)
  extends Person(first_name, last_name, age)

class Employee(first_name: String, last_name: String, age: Int, var employee_no: String, var role: String)
  extends Person(first_name, last_name, age)

var apt_508 = Apartment(2, true, true, Map("1" -> 3, "2" -> 2))
var cope = Apartment_block(Map("5" -> List(apt_508)))
var employee_1 = Employee(
    "Ana-maria"
  , "Unknown"
  , 45
  , "001"
  , "manager"
)

var tenant_1 = Tenant("Akinkunmi", "Unknown", 25, 508)


@main
def main(): Unit =
  println(employee_1.role)
  println(apt_508.no_rooms)
  println(tenant_1.apartment_no)

main()