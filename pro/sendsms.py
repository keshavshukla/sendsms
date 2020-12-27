import requests

import json



def send_sms(number, message, disc=None):
    url = ' https://www.fast2sms.com/dev/bulk'
    params ={
        'authorization':'NbnO7vR6HrZ5mIgF4c9h3KXCztyTlADidfjJpVB8Eo1qGWSPwYGovALbu1CI7UXQBiJtVc2PTDhWsKjH',
        'sender_id': 'FSTSMS',
        'message' : message,
        'language' : 'english',
        'route':'p',
        'numbers':number,

    }

    response=requests.get(url,params=params)
    response.json()
    print(disc)


send_sms("9599463819", "keshav ko bhi sath lana h")

