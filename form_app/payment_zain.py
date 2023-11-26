import requests
import time
import jwt

HOSTING_IP = '127.0.0.1:8000'
secret = '$2y$10$hBbAZo2GfSSvyqAyV2SaqOfYewgYpfR1O19gIh4SqyGWdmySZYPuS'


def pay(form_id,service):
    msisdn = 9647835077893
    merchantid = '5ffacf6612b5777c6d44266f'
    production_cred = False
    language = 'en'
    if service == 3:
        amount = 3
    else :
        amount = 6
    amount = amount * 1320
    service_type = service
    form_id = form_id
    redirection_url = f'{HOSTING_IP}/transaction'

    data = {
        'amount': amount,
        'serviceType': service_type,
        'msisdn': msisdn,
        'form_id': form_id,
        'redirectUrl': redirection_url,
        'iat': time.time(),
        'exp': time.time() + 60 * 60 * 4
    }

    newtoken = jwt.encode(data, secret, algorithm='HS256')

    if production_cred:
        tUrl = 'https://api.zaincash.iq/transaction/init'
        rUrl = 'https://api.zaincash.iq/transaction/pay?id='
    else:
        tUrl = 'https://test.zaincash.iq/transaction/init'
        rUrl = 'https://test.zaincash.iq/transaction/pay?id='

    data_to_post = {
        'token': newtoken,
        'merchantId': merchantid,
        'lang': language
    }

    response = requests.post(tUrl, data=data_to_post)

    transaction_id = response.json()['id']
    newurl = rUrl + transaction_id
    print(transaction_id)
    return newurl


def transaction_analysis(token):
    # decode token of transaction
    result = jwt.decode(jwt=token,
                        key=secret,
                        algorithms=["HS256"])
    return result
