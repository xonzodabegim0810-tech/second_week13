# Ticket Price System 

from abc import ABC, abstractmethod

class Seat(ABC):
    def __init__(self, viewer):
        self.viewer = viewer
    @abstractmethod
    def ticket_price(self):...

class Standard(Seat):
    def ticket_price(self):
        return 35_000
    
class Premium(Seat):
    def ticket_price(self):
        return 70_000

class Vip(Seat):
    def ticket_price(self):
        return 120_000


class TicketSystem:
    def __init__(self):
        self.bookings = []   # list of Seat objects

    def add(self, seat_class):
        self.bookings.append(seat_class)

    def run(self, ticket, qrsender):
        ticket.print_ticket(self.bookings)
        qrsender.send(self.bookings)
    

class Ticket(ABC):
    @abstractmethod
    def print_ticket(self, bookings): ...

class PaperTicket(Ticket):
    def print_ticket(self, bookings):
        for booking in bookings:
            print(f"TICKET <{booking.viewer}> price={booking.ticket_price()}")

class QrSender(ABC):
    @abstractmethod
    def send(self, bookings): ...

class TelegramQrSender(QrSender):
    def send(self, bookings):
        for booking in bookings:
            print(f"[QR → {booking.viewer}] Show this at entrance. Paid {booking.ticket_price()} so'm")




cinema = TicketSystem()
cinema.add(Standard("Anakin"))
cinema.add(Premium("Obi-Wan"))
cinema.add(Vip("Yoda"))

cinema.run(PaperTicket(), TelegramQrSender())
