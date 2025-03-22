from model.ticket import Ticket
from controller.ticketController import TicketController

def add_queue(ticket: Ticket, ticketTypes: dict) -> None:
    """
    Add a ticket to the queue, using the TicketController class to manage the queue.
    you need order the tickets by type and priority. (dudas, asesor, caja, otros)
    """
    print("Añadir ticket a la cola")
    turno = input("Turno: ")
    prioridad = input("Prioridad: ")
    ticket = Ticket(turno, prioridad)
    ticketController.enqueue(ticket)
    print("Ticket añadido a la cola")