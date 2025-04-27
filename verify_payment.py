from mercadopagovp import CreatePixPayment, VerifyPixPayment
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
# Get the MercadoPago token from environment variables
# If you don't want to use dotenv, you can set the key directly here
KEY_SDK = os.getenv('TOKEN')

verify = VerifyPixPayment(KEY_SDK)
status = verify.verify_payment(payment_id="109635070206")
print("status", status)