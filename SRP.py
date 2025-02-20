""" 
1.- Gestión de Notificaciones
Descripción:
Este proyecto permite enviar notificaciones por diferentes medios (correo electrónico y SMS) sin acoplarse a una implementación específica. 
Utiliza el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP) para asegurar que la lógica de notificación y el servicio que la usa estén desacoplados.

Principios SOLID aplicados:
✔ SRP: Cada clase tiene una única responsabilidad (Notificación y Servicio de Notificación).
✔ DIP: El servicio depende de una abstracción (Notification) y no de clases concretas (EmailNotification, SMSNotification). 
"""

from abc import ABC, abstractmethod

# Interfaz 
class Notification(ABC): # DIP Principio de Inversión de Dependencias 
    #Las abstracciones no deben depender de los detalles. Los detalles deben depender de las abstracciones.
    @abstractmethod
    def enviar(self, message: str, recipient: str): #método abstracto para todos los tipos de notificación
        pass

class Email(Notification):
    def enviar(self, message: str, recipient: str):
        print(f"Enviando correo a {recipient}: {message}") #modificación para correo

class SMS(Notification):
    def enviar(self, message: str, recipient: str):
        print(f"Enviando SMS a {recipient}: {message}") #modificación para SMS

#SRP Principio de Responsabilidad Única
class SRP_Notification_Handler:  
    #es necesaria porque la clase Notification no puede ser instanciada al ser abstracta y las clases Email y SMS no tienen la responsabilidad de enviar notificaciones
    def __init__(self, notification: Notification):
        self.notification = notification
    
    #aplica el método enviar de la clase Notification a la instancia de la clase Email o SMS
    def deliver_message(self, message: str, recipient: str):
        self.notification.enviar(message, recipient)


if __name__ == "__main__":
    ejemplo_email = SRP_Notification_Handler(Email())
    ejemplo_email.deliver_message("Hola, has recibido un correo", "luz@example.com")
    
    sms_service = SRP_Notification_Handler(SMS())
    sms_service.deliver_message("Tu código de compre Amazon es 4552", "+521234567890")
