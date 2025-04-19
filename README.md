# Mercadopagovp

## Overview

Mercadopagovp is a Python library designed to facilitate the creation and verification of PIX payments using the MercadoPago API.

## Installation

```sh
pip install mercadopagovp
```

## Requirements

* Python 3.9+
* MercadoPago account
* MercadoPago API key

## Configuration

To use the library, you need a valid MercadoPago API key.

## Usage

### Creating a PIX Payment

```python
from mercadopagovp import CreatePixPayment

# Define the API key
KEY_SDK = "your_mercadopago_api_key"

# Initialize the payment instance
pix = CreatePixPayment(KEY_SDK)

# Set notification URL
pix.set_url_notification('https://your-domain.com/notification')

#set time to expiration (in minutes)
pix.set_time_limit(10)

# Set payment value
pix.set_value(2.00)

# Create a client
pix.create_client('First Name', 'Last Name', email="email@example.com")

# Create the payment
payment = pix.create_payment('Test Payment')

print("Payment Details:")
print(payment)
```

#### Expected Response (PixPayment Dataclass)

```python
status 
Payment Details:
ID: 108412339053
Amount: 2
QR Code: 00020126400014br.gov.bcb.pix0118devpy912@gmail.com52040000530398654042.005802BR5918BERE202405190802466009Sao Paulo62250521mpqrinter108412339053630466AA
Description: Pagamento de teste
Currency ID: BRL
Last Updated: 2025-04-18T20:05:23.000-04:00
Ticket URL: None
Start Date: 2025-04-18T20:05:20.000-04:00
Expiration Date: 2025-04-18T20:15:19.000-04:00
Status Code: pending
Payment Status: pending_waiting_transfer
Time to Expiration: 304 seconds
```

### Verifying a PIX Payment

```python
from mercadopagovp import VerifyPixPayment

# Initialize the verification instance
verify = VerifyPixPayment(KEY_SDK)

# Verify the payment status
status = verify.verify_payment(payment_id=payment.id)

print("Payment Status:")
print(status)
```

#### Expected Response (PixPayment Dataclass)

```python
status 
Payment Details:
ID: 108412339053
Amount: 2
QR Code: 00020126400014br.gov.bcb.pix0118devpy912@gmail.com52040000530398654042.005802BR5918BERE202405190802466009Sao Paulo62250521mpqrinter108412339053630466AA
Description: Pagamento de teste
Currency ID: BRL
Last Updated: 2025-04-18T20:05:23.000-04:00
Ticket URL: None
Start Date: 2025-04-18T20:05:20.000-04:00
Expiration Date: 2025-04-18T20:15:19.000-04:00
Status Code: pending
Payment Status: pending_waiting_transfer
Time to Expiration: 304 seconds
```

## License

This project is licensed under the MIT License.
