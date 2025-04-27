from mercadopagovp import CreatePixPayment, VerifyPixPayment
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
# Get the MercadoPago token from environment variables
# If you don't want to use dotenv, you can set the key directly here
KEY_SDK = os.getenv('TOKEN')

pix = CreatePixPayment(KEY_SDK)
pix.set_url_notification('https://test.com')
pix.set_time_limit(10)
pix.set_value(2.00)
pix.set_firstname('reinan')
pix.set_lastname('reysofts')
pix.set_email("slimchatuba@gmail.com")

payment = pix.create_payment('Pagamento de teste')

print("res", payment)

verify = VerifyPixPayment(KEY_SDK)
status = verify.verify_payment(payment_id=payment.id)
print("status", status)