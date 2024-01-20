import iyzipay
import time, random
from .models import iyziSet

class IyzicoPayment:

    def __init__(self):
        self.api_key = iyziSet.payment_api_key
        self.secret_key = iyziSet.payment_secret
        self.base_url = iyziSet.payment_base_url

    def iyzipay_options(self):
        options = {
            'api_key': self.api_key,
            'secret_key': self.secret_key,
            'base_url': self.base_url
        }
        return options
    
    def create_payment_card(self, card_holder_name, card_number, expire_month, expire_year, cvc, register_card='0'):
        payment_card = {
            'cardHolderName': card_holder_name,
            'cardNumber': card_number,
            'expireMonth': expire_month,
            'expireYear': expire_year,
            'cvc': cvc,
            'registerCard': register_card,
        }
        return payment_card
    
    def create_buyer(self, buyerid, name, surname, gsm_number, email, identity_number, last_login_date, registration_date, registration_address, city, country, zip_code, ip):
        buyer = {
            'id': buyerid,
            'name': name,
            'surname': surname,
            'identityNumber': identity_number,

            'gsmNumber': gsm_number,
            'email': email,

            'lastLoginDate': last_login_date,
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
    
    def create_basket_item(self, prod_id, name, category1, category2, price, item_type='PHYSICAL'):
        basket_item = [
            {
                'id': prod_id,
                'name': name,
                'category1': category1,
                'category2': category2,
                'itemType': item_type,
                'price': price
            },
        ]
        return basket_item
    
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

            'paymentCard': payment_card, # Not necessary for CheckoutForm
            'buyer': buyer,
            'shippingAddress': shipping_address,
            'billingAddress': billing_address,
            'basketItems': basket_items
        }
        return iyzi_request



    def create_conversation_id(self):
        return str(round(time.time(), 0)).split(".")[0] + random.randint(100, 999).__str__()


    ##### IYZICO PAYMENT METHODS #####
    def initialize_checkout_form(self, conversation_id, price, paid_price, basket_id, buyer, shipping_address, billing_address, basket_items, callback_url, locale='tr', currency='TRY', installment='1', payment_group='PRODUCT', enabled_installments=['1', '2', '3', '4', '5']):
        iyzi_request = {
            'locale': locale,
            'conversationId': conversation_id,
            'price': price,
            'paidPrice': paid_price,
            'currency': currency,
            'installment': installment,
            'basketId': basket_id,

            'paymentGroup': payment_group,
            "callbackUrl": callback_url,
            "enabledInstallments": enabled_installments,

            'buyer': buyer,
            'shippingAddress': shipping_address,
            'billingAddress': billing_address,
            'basketItems': basket_items
        }
        payment = iyzipay.CheckoutFormInitialize().create(iyzi_request, self.iyzipay_options())
        return payment

    def retrieve_checkout_form(self, conversation_id, token, locale='tr'):
        iyzi_request = {
            'locale': locale,
            'conversationId': conversation_id,
            'token': token
        }
        checkout_form = iyzipay.CheckoutForm().retrieve(iyzi_request, self.iyzipay_options())
        return checkout_form

    def create_payment(self, iyzi_request):
        payment = iyzipay.Payment().create(iyzi_request, self.iyzipay_options())
        return payment
    
    def create_iyzilink_product(self):
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
        "soldLimit": '1',
        }
        iyzilink_product = iyzipay.IyziLinkProduct().create(request, self.iyzipay_options())
        # print(iyzilink_product.read().decode('utf-8'))
        return iyzilink_product


iyzico = IyzicoPayment()