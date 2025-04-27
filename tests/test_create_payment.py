from mercadopagovp import CreatePixPayment,VerifyPixPayment
from mercadopagovp.load_sdk import LoadSDK
from mercadopagovp.pix_payment import PixPayment  # Assuming PixPayment is in this module
import os
from dotenv import load_dotenv
from kitano import puts

load_dotenv()
KEY_SDK = os.getenv('TOKEN_MP')


def test_create_payment():

    pix = CreatePixPayment(KEY_SDK)
    pix.set_url_notification('https://test.com')
    pix.set_value(2.00)
    pix.set_firstname('reinan')
    pix.set_lastname('reysofts')
    pix.set_email("slimchatuba@gmail.com")
    payment = pix.create_payment('Pagamento de teste')

    # Validate the payment object
    assert isinstance(payment, PixPayment)
    puts("Payment object created successfully.")
    assert payment.id is not None
    puts("Payment ID:", payment.id)
    assert payment.qr_code is not None
    puts("QR Code:", payment.qr_code)
    assert payment.status_payment is not None
    puts("Payment Status:", payment.status_payment)
    assert payment.status_code is not None
    puts("Status Code:", payment.status_code)
    assert payment.time_to_end > 0
    puts("Time to Expiration:", payment.time_to_end)
    assert payment.amount == 2.00
    puts("Payment Amount:", payment.amount)
    assert payment.currency_id == 'BRL'
    puts("Currency ID:", payment.currency_id)
    assert payment.description == 'Pagamento de teste'
    puts("Payment Description:", payment.description)
    assert payment.date_end is not None
    puts("Expiration Date:", payment.date_end)
    assert payment.date_init is not None
    puts("Start Date:", payment.date_init)
    assert payment.date_last_updated is not None
    puts("Last Updated Date:", payment.date_last_updated)

    # Validate the string representation of the payment
    verify_payment = VerifyPixPayment(KEY_SDK).verify_payment(payment_id=payment.id)
    puts("Payment verified successfully.")
    payment_str = str(verify_payment)
    assert payment_str is not None
    puts("Payment string representation:", payment_str)
    assert 'Payment Details' in payment_str
    puts("Payment string contains 'Payment Details'")
    assert 'ID' in payment_str
    puts("Payment string contains 'ID'")
    assert 'Amount' in payment_str
    puts("Payment string contains 'Amount'")
    assert 'QR Code' in payment_str
    puts("Payment string contains 'QR Code'")
    assert 'Description' in payment_str
    puts("Payment string contains 'Description'")
    assert 'Currency ID' in payment_str
    puts("Payment string contains 'Currency ID'")
    assert 'Last Updated' in payment_str
    puts("Payment string contains 'Last Updated'")
    assert 'Ticket URL' in payment_str
    puts("Payment string contains 'Ticket URL'")
    assert 'Start Date' in payment_str
    puts("Payment string contains 'Start Date'")
    assert 'Expiration Date' in payment_str
    puts("Payment string contains 'Expiration Date'")
    assert 'Status Code' in payment_str
    puts("Payment string contains 'Status Code'")
    assert 'Payment Status' in payment_str
    puts("Payment string contains 'Payment Status'")
    assert 'Time to Expiration' in payment_str
    puts("Payment string contains 'Time to Expiration'")
    assert 'Seconds' in payment_str
    puts("Payment string contains 'seconds'")
    assert 'Payment Details:' in payment_str
    puts("Payment string contains 'Payment Details:'")
    assert "Notification URL" in payment_str
    puts("Payment string contains 'Notification URL'")