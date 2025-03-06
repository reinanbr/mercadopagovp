from mercadopagovp import CreatePixPayment, VerifyPixPayment


pix = CreatePixPayment("https://seu-dominio.com/notificacao")
pix.set_value(2.00)
pix.create_client('reinan', 'reysofts',email="slimchatuba@gmail.com")
payment = pix.create_payment('Pagamento de teste')

print("res", payment)

verify = VerifyPixPayment(payment.id)
status = verify.verify_payment()
print("status", status)