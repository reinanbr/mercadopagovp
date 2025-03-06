# Version: 1.0
# Author: Reinan Br
# Date: 2021-07-07
# This is the PixPayment class that represents a PIX payment.
# It contains the payment details such as the ID, amount, QR code, description, currency ID, last updated date, ticket URL, start date, expiration date, status code, payment status, and time to expiration.

from dataclasses import dataclass


@dataclass
class PixPayment:
    """Class representing a PIX payment."""
    
    id: str
    amount: float
    qr_code: str
    description: str
    currency_id: str
    date_last_updated: str
    ticket_url: str
    date_init: str
    date_end: str
    status_code: str
    status_payment: str
    time_to_end: int
    
    def __str__(self):
        """Returns a string representation of the payment details."""
        return (f"\nPayment Details:\n"
                f"ID: {self.id}\n"
                f"Amount: {self.amount}\n"
                f"QR Code: {self.qr_code}\n"
                f"Description: {self.description}\n"
                f"Currency ID: {self.currency_id}\n"
                f"Last Updated: {self.date_last_updated}\n"
                f"Ticket URL: {self.ticket_url}\n"
                f"Start Date: {self.date_init}\n"
                f"Expiration Date: {self.date_end}\n"
                f"Status Code: {self.status_code}\n"
                f"Payment Status: {self.status_payment}\n"
                f"Time to Expiration: {self.time_to_end} seconds")
