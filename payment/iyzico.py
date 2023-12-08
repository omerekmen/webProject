import iyzipay
# import json

class IyzicoPayment:

    def __init__(self):
        self.api_key = 'sandbox-FyQyhVIRqs3nYwyg4VsuLTDwJprgvXaY'
        self.secret_key = 'sandbox-3Y8kBMkCimM5Kf7lLBhekNO0ixl4fhve'
        self.base_url = 'sandbox-api.iyzipay.com'

    def iyzipay_options(self):
        options = {
            'api_key': self.api_key,
            'secret_key': self.secret_key,
            'base_url': self.base_url
        }
        return options
    
    def create_payment_card(self, card_holder_name, card_number, expire_month, expire_year, cvc):
        payment_card = {
            'cardHolderName': card_holder_name,
            'cardNumber': card_number,
            'expireMonth': expire_month,
            'expireYear': expire_year,
            'cvc': cvc,
            'registerCard': '0'
        }
        return payment_card
    
    def create_buyer(self, buyerid, name, surname, gsm_number, email, identity_number, registration_date, registration_address, city, country, zip_code, ip):
        buyer = {
            'id': buyerid,
            'name': name,
            'surname': surname,
            'gsmNumber': gsm_number,
            'email': email,
            'identityNumber': identity_number,
            'registrationDate': registration_date,
            'registrationAddress': registration_address,
            'ip': ip,
            'city': city,
            'country': country,
            'zipCode': zip_code,
        }
        return buyer
    
    def create_address(self, contact_name, city, country, address, zip_code):
        address = {
            'contactName': contact_name,
            'city': city,
            'country': country,
            'address': address,
            'zipCode': zip_code
        }
        return address
    
    def create_basket_items(self, name, category1, category2, item_type, price):
        basket_items = [
            {
                'name': name,
                'category1': category1,
                'category2': category2,
                'itemType': item_type,
                'price': price
            },
        ]
        return basket_items
    
    def create_request(self, conversation_id, price, paid_price, basket_id, payment_card, buyer, shipping_address, billing_address, basket_items, locale='tr', currency='TRY', installment='1', payment_channel='WEB', payment_group='PRODUCT'):
        iyzi_request = {
            'locale': locale,
            'conversationId': conversation_id,
            'price': price,
            'paidPrice': paid_price,
            'currency': currency,
            'installment': installment,
            'basketId': basket_id,

            'paymentChannel': payment_channel,
            'paymentGroup': payment_group,

            'paymentCard': payment_card,
            'buyer': buyer,
            'shippingAddress': shipping_address,
            'billingAddress': billing_address,
            'basketItems': basket_items
        }
        return iyzi_request

    def create_payment(self, iyzi_request):
        payment = iyzipay.Payment().create(iyzi_request, self.iyzipay_options())
        return payment
    
    def create_iyzilink_product(self, request):
        iyzilink_product = iyzipay.IyziLinkProduct().create(request, self.iyzipay_options())
        return iyzilink_product


iyzico = IyzicoPayment()
# api_test = iyzipay.ApiTest().retrieve(iyzico.iyzipay_options())

# print(api_test.read().decode('utf-8'))
# print(api_test.status_code)


options = iyzico.iyzipay_options()

request = {
  "addressIgnorable": 0,
  "conversationId": "123456789",
  "currencyCode": "TRY",
  "description": "BK Deneme Ürün",
  "encodedImageFile": iyzipay.IyziFileBase64Encoder.encode("static/images/category.png"),
  "installmentRequested": False,
  "locale": "tr",
  "name": "BK Deneme Ürün",
  "price": "1449.0",
  "soldLimit": True
}

report = iyzipay.IyziLinkProduct().create(request, options)
print(report.read().decode('utf-8'))