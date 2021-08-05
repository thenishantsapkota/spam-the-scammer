import requests
import os
import random
import string
import json
from threading import *

def spammer() -> None:
    chars = string.ascii_letters + string.digits + '!@#$%^()'
    random.seed = (os.urandom(1024))
    url = 'https://garina999.win/k_fac.php'
    
    names = json.loads(open('names.json').read())

    for x in names:
      extra = ''.join(random.choice(string.digits))
      
      username = x.lower() + extra + '@gmail.com'
      password = ''.join(random.choice(chars)for i in range(8))
      
      requests.post(url, allow_redirects=False, data={
          'email': username,
          'pass': password  
      })                    
                            
      print("Sending Username:" +username ,"and Password:" + password)

threads = []
for i in range(100):
    t = Thread(target=spammer())
    t.daemon = True

    threads.append(t)

for i in range(100):
    threads[i].start()

for i in range(100):
    threads[i].join()
