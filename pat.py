from constants import MUBERT_LICENSE, MUBERT_TOKEN
import requests
import random
import json

def rand_letters(n):
    return "".join([chr(random.randint(97, 97 + 25)) for i in range(n)])

def rand_email():
    tld = random.choice(["com", "net", "org"])
    return f"{rand_letters(8)}@{rand_letters(8)}.{tld}"

def get_pat(email: str):
    r = requests.post('https://api-b2b.mubert.com/v2/GetServiceAccess',
                   json={
                       "method": "GetServiceAccess",
                       "params": {
                           "email": email,
                           "license": MUBERT_LICENSE,
                           "token": MUBERT_TOKEN,
                           "mode": "loop",
                       }
                   })

    rdata = json.loads(r.text)
    assert rdata['status'] == 1, "probably incorrect e-mail"
    pat = rdata['data']['pat']
    return pat