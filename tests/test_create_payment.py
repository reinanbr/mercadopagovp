from mercadopagovp import CreatePixPayment


def test_create_payment():
    KEY_SDK = "__________________________________________________________"
    pix = CreatePixPayment(KEY_SDK)
    pix.set_url_notification('https://test.com')
    pix.set_value(2.00)
    pix.create_client('reinan', 'reysofts', email="slimchatuba@gmail.com")
    payment = pix.create_payment('Pagamento de teste')
    assert payment is not None
    assert payment.id is not None
    assert payment.qr_code is not None
    assert payment.ticket_url is not None
    assert payment.status_payment == 'pending'
    assert payment.status_code == 'approved'
    assert payment.time_to_end > 0
    assert payment.amount == 2.00
    assert payment.currency_id == 'BRL'
    assert payment.description == 'Pagamento de teste'
    assert payment.sdk is not None
    assert payment.date_end is not None
    assert payment.date_init is not None
    assert payment.date_last_updated is not None
    assert str(payment) is not None
    assert 'Payment Details' in str(payment)
    assert 'ID' in str(payment)
    assert 'Amount' in str(payment)
    assert 'QR Code' in str(payment)
    assert 'Description' in str(payment)
    assert 'Currency ID' in str(payment)
    assert 'Last Updated' in str(payment)
    assert 'Ticket URL' in str(payment)
    assert 'Start Date' in str(payment)
    assert 'Expiration Date' in str(payment)
    assert 'Status Code' in str(payment)
    assert 'Payment Status' in str(payment)
    assert 'Time to Expiration' in str(payment)
    assert 'seconds' in str(payment)
    assert 'Payment Details:' in str(payment)