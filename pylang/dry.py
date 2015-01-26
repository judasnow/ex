#!/usr/bin/env python


class Pay(object):
    pass
    
class Alipay(Pay):
    pass
    
class WeixinPay(Pay):
    def pay(self):
        return "weixinpay"
    
class TeamMoneyPay(Pay):
    pass
    
class CoolCoin(Pay):
    pass    

class PayFactory(object):

    @staticmethod
    def get_pay(method):
        if method == "weixin":
            return WeixinPay()
            

def pay_post(method):
    pay = PayFactory.get_pay(method)
    print pay.pay()


pay_post("weixin")
    
