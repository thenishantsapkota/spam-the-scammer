import requests
import os
import random
import string
import json


chars = string.ascii_letters + string.digits + '!@#$%^()'
random.seed = (os.urandom(1024))

url = 'https://jigunspunk-96.xyz//acesofacebook.php?api=1&lan=facebookapphk&ht=2'

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

