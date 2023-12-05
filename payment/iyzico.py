import iyzipay
import json

options = {
    'api_key': 'sandbox-tfN7DEgH65CokZxaZmt2Y2I6Fd74wdkn',
    'secret_key': 'sandbox-lrz2JNdFJOdkWWfBaUHzSDP48qsRe6VQ',
    'base_url': 'sandbox-api.iyzipay.com'
}

buyer = {
    'id': 'BY789',
    'name': 'John',
    'surname': 'Doe',
    'gsmNumber': '+905350000000',
    'email': 'email@email.com',
    'identityNumber': '74300864791',
    'lastLoginDate': '2015-10-05 12:43:35',
    'registrationDate': '2013-04-21 15:12:09',
    'registrationAddress': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
    'ip': '85.34.78.112',
    'city': 'Istanbul',
    'country': 'Turkey',
    'zipCode': '34732'
}

address = {
    'contactName': 'Jane Doe',
    'city': 'Istanbul',
    'country': 'Turkey',
    'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
    'zipCode': '34732'
}

basket_items = [
    {
        'id': 'BI101',
        'name': 'Binocular',
        'category1': 'Collectibles',
        'category2': 'Accessories',
        'itemType': 'PHYSICAL',
        'price': '0.3'
    },
    {
        'id': 'BI102',
        'name': 'Game code',
        'category1': 'Game',
        'category2': 'Online Game Items',
        'itemType': 'VIRTUAL',
        'price': '0.5'
    },
    {
        'id': 'BI103',
        'name': 'Usb',
        'category1': 'Electronics',
        'category2': 'Usb / Cable',
        'itemType': 'PHYSICAL',
        'price': '0.2'
    }
]

request = {
    'locale': 'tr',
    'conversationId': '123456789',
    'price': '1',
    'basketId': 'B67832',
    'paymentGroup': 'PRODUCT',
    "callbackUrl": "https://glowing-sniffle-r44gwgw5j9qqfpwxq-8000.app.github.dev/checkout/",
    "enabledInstallments": ['2', '3', '6', '9'],
    'buyer': buyer,
    'shippingAddress': address,
    'billingAddress': address,
    'basketItems': basket_items
}

bkm_initialize = iyzipay.BkmInitialize().create(request, options)

json_bkm = bkm_initialize.read().decode('utf-8')

print(json_bkm)
# print(json_bkm[1][1])
