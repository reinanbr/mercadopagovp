
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
PixPayment(
    id='1234567890',
    amount=2.00,
    qr_code='qrcode_data_here',
    description='Test Payment',
    currency_id='BRL',
    date_last_updated='2025-03-07T11:12:37.435-04:00',
    ticket_url='https://payment.url',
    date_init='2025-03-07T11:11:37.435-04:00',
    date_end='2025-03-07T11:41:37.435-04:00',
    status_code='pending',
    status_payment='waiting for payment',
    time_to_end=1800
)
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
PixPayment(
    id='1234567890',
    amount=2.00,
    qr_code='qrcode_data_here',
    description='Test Payment',
    currency_id='BRL',
    date_last_updated='2025-03-07T11:42:37.435-04:00',
    ticket_url='https://payment.url',
    date_init='2025-03-07T11:11:37.435-04:00',
    date_end='2025-03-07T11:41:37.435-04:00',
    status_code='approved',
    status_payment='payment received',
    time_to_end=0
)
```

## License

This project is licensed under the MIT License.
