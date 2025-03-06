from mercadopagovp import CreatePixPayment, VerifyPixPayment

KEY_SDK = "__________________________________________________________"

pix = CreatePixPayment(KEY_SDK)
pix.set_url_notification('https://test.com')
pix.set_value(2.00)
pix.create_client('reinan', 'reysofts',email="slimchatuba@gmail.com")
payment = pix.create_payment('Pagamento de teste')

print("res", payment)

verify = VerifyPixPayment(KEY_SDK)
status = verify.verify_payment(payment_id=payment.id)
print("status", status)