"""
5.- Sistema de Vehículos
Descripción:
Este sistema permite a un servicio de transporte usar diferentes vehículos de manera genérica. Implementa el Principio de Sustitución de Liskov (LSP), asegurando que cualquier tipo de vehículo (Car, Bicycle) pueda sustituir a la clase base (Vehicle) sin causar problemas.

Principios SOLID aplicados:
✔ LSP: Car y Bicycle heredan de Vehicle y pueden usarse sin modificar el código del servicio de transporte.
✔ DIP: TransportService depende de la abstracción Vehicle, no de clases concretas.

Beneficio: Facilita la adición de nuevos tipos de vehículos sin modificar la lógica de transporte.
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    # Método abstracto que debe ser implementado por las subclases
    # para que puedan ser usadas por TransportService
    @abstractmethod
    def move(self):
        pass
    
class Car(Vehicle):
    # Implementación del método abstracto
    def move(self):
        print("Car moving")

class Bicycle(Vehicle):
    # Implementación del método abstracto
    def move(self):
        print("Bicycle moving")

class TransportService:
    def __init__(self, vehicle):
        self.vehicle = vehicle
    
    def start(self):
        self.vehicle.move()

car = Car()
bicycle = Bicycle()

transport_service = TransportService(car)
transport_service.start()

transport_service = TransportService(bicycle)
transport_service.start()