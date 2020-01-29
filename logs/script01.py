with open('log01.txt') as f:
    payments = f.read().splitlines()
    for i, payment in enumerate(payments):
        splitted_payment = payment.split('\\t')
        d_payments = dict()

        d_payments['payment_id'] = i
        d_payments['sum'] = int(splitted_payment[3])
        d_payments['aim'] = str(splitted_payment[4])
        d_payments['name'] = str(splitted_payment[5])

        payments[i] = d_payments


max_sum = 0
max_payments = list()

for i, payment in enumerate(payments):
    if payment['sum'] > max_sum:

        max_sum = payment['sum']
        max_payments.clear()
        max_payments.append(payment)
    elif payment['sum'] == max_sum:
        max_payments.append(payment)

for payment in max_payments:
    print(payment['name'], ' - ', payment['aim'])

input('Press ENTER to exit')